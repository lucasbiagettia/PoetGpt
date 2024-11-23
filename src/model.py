from transformers import GPTNeoXForCausalLM, AutoTokenizer
from src.config import DEFAULT_GENERATION_ARGS

def load_model_and_tokenizer(repo_name):
    model = GPTNeoXForCausalLM.from_pretrained(repo_name)
    tokenizer = AutoTokenizer.from_pretrained(repo_name)
    return model, tokenizer

def generate_poem(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    tokens = model.generate(**inputs, **DEFAULT_GENERATION_ARGS)
    poem = tokenizer.decode(tokens[0], skip_special_tokens=True)
    return clean_generated_text(poem)

def clean_generated_text(text):
    text = text.strip()
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return "\n\n".join(paragraphs)

