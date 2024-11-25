
from huggingface_hub import login
from transformers import GPTNeoXConfig, GPTNeoXForCausalLM, AutoTokenizer, AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer, get_scheduler, EarlyStoppingCallback
from torch.optim import AdamW 
from datasets import load_from_disk, Dataset, DatasetDict
import zipfile
import torch

#
# Get Model
#

my_repo_name = "lucasbiagettia/GPTNeoX-spanish_poet"


model = GPTNeoXForCausalLM.from_pretrained(my_repo_name)
tokenizer = AutoTokenizer.from_pretrained(my_repo_name)

#
# Define preprocess algorithm
#

max_len = 64

START_OF_POEM = tokenizer.bos_token
END_OF_POEM = tokenizer.eos_token
START_OF_STANZA = "<|startofstanza|>"
END_OF_STANZA = "<|endofstanza|>"
START_OF_VERSE = "<|startofverse|>"
END_OF_VERSE = "<|endofverse|>"

def preprocess_poem_with_stanzas(poem):
    stanzas = poem.strip().split("\n\n")  # Dividir el poema en estrofas
    processed_poem = f"{START_OF_POEM}\n"
    for stanza in stanzas:
        processed_poem += f"{START_OF_STANZA}\n"
        lines = stanza.strip().split("\n")
        for line in lines:
            processed_poem += f"{START_OF_VERSE}{line.strip()}{END_OF_VERSE}\n"
        processed_poem += f"{END_OF_STANZA}\n"
    processed_poem += f"{END_OF_POEM}\n"
    return processed_poem

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding='max_length', max_length=max_len)

#
# Load and process Dataset
#

zip_path = '/content/corpus.zip'

poem_contents = []
with zipfile.ZipFile(zip_path, 'r') as z:
      for file_name in z.namelist():
          if file_name.endswith('.txt'):
              with z.open(file_name) as f:
                  poem_contents.append(f.read().decode('utf-8'))

processed_poems = [preprocess_poem_with_stanzas(poem) for poem in poem_contents]

dataset = Dataset.from_dict({'text': processed_poems})

train_test_split = dataset.train_test_split(test_size=0.2, shuffle=True, seed=42)

dataset_dict = DatasetDict({
      'train': train_test_split['train'],
      'validation': train_test_split['test']
  })

tokenized_datasets = dataset_dict.map(
    tokenize_function,
    batched=True,
    num_proc=4,
    remove_columns=["text"]
  )


data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

#
# Initialize training variables and train
#

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model.to(device)

optimizer = AdamW(model.parameters(), lr=5e-4, weight_decay=0.01)  

early_stopping_callback = EarlyStoppingCallback(
    early_stopping_patience=5,  
    early_stopping_threshold=0.01 

training_args = TrainingArguments(
    output_dir="./results2",
    per_device_train_batch_size=128,
    per_device_eval_batch_size=128,  
    gradient_accumulation_steps=2,  
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=2,
    save_steps=1000,
    fp16=True,  
    remove_unused_columns=True,
    dataloader_num_workers=4,  
    gradient_checkpointing=False,  
    fp16_full_eval=True,  
    eval_strategy="steps",
    eval_steps=20,  
    load_best_model_at_end=True, 
    metric_for_best_model="eval_loss", 
    greater_is_better=False 
)


num_training_steps = len(tokenized_datasets['train']) // (training_args.per_device_train_batch_size * training_args.gradient_accumulation_steps) * int(training_args.num_train_epochs)

lr_scheduler = get_scheduler(
    name="linear",
    optimizer=optimizer,
    num_warmup_steps=0,
    num_training_steps=num_training_steps
)

def compute_metrics(eval_pred):
    loss = eval_pred.metrics["eval_loss"]
    return {"eval_loss": loss}

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
    data_collator=data_collator,
    compute_metrics=None,
    optimizers=(optimizer, lr_scheduler),
    callbacks=[early_stopping_callback]
)

trainer.train()

