from src.config import START_OF_POEM, END_OF_POEM, START_OF_STANZA, END_OF_STANZA, START_OF_VERSE, END_OF_VERSE

def preprocess_poem_with_stanzas(poem, start_poem=START_OF_POEM, end_poem=END_OF_POEM, start_stanza=START_OF_STANZA, end_stanza=END_OF_STANZA, start_verse=START_OF_VERSE, end_verse=END_OF_VERSE):
    stanzas = poem.strip().split("\n\n")
    processed_poem = f"{start_poem}\n"
    for stanza in stanzas:
        processed_poem += f"{start_stanza}\n"
        lines = stanza.strip().split("\n")
        for line in lines:
            processed_poem += f"{start_verse}{line.strip()}{end_verse}\n"
        processed_poem += f"{end_stanza}\n"
    return processed_poem
