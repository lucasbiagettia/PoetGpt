#Definición original del modelo vacío a partir de pythia
from transformers import GPTNeoXConfig, GPTNeoXForCausalLM, AutoTokenizer

model_name = "EleutherAI/pythia-160m"


tokenizer = AutoTokenizer.from_pretrained(model_name)

special_tokens = {
    "pad_token": "<|pad|>",
    "eos_token": "<|endofpoem|>",
    "bos_token": "<|startofpoem|>",
    "additional_special_tokens": [
        "<|startofstanza|>",
        "<|endofstanza|>",
        "<|startofverse|>",
        "<|endofverse|>"
    ]
}
tokenizer.add_special_tokens(special_tokens)
config = GPTNeoXConfig.from_pretrained(model_name)
config.pad_token_id = tokenizer.pad_token_id
config.eos_token_id = tokenizer.eos_token_id
config.bos_token_id = tokenizer.bos_token_id
model = GPTNeoXForCausalLM(config)

