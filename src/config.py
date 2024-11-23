START_OF_POEM = "<|startofpoem|>"
END_OF_POEM = "<|endofpoem|>"
START_OF_STANZA = "<|startofstanza|>"
END_OF_STANZA = "<|endofstanza|>"
START_OF_VERSE = "<|startofverse|>"
END_OF_VERSE = "<|endofverse|>"

DEFAULT_GENERATION_ARGS = {
    "max_length": 512,
    "min_length": 32,
    "temperature": 0.7,
    "top_k": 50,
    "top_p": 0.8,
    "do_sample": True,
    "repetition_penalty": 1.2,
    "eos_token_id": [50281, 50278]
}
