from transformers import pipeline
import time


# small grouped-entities NER pipeline for dev. Replace model with anything from HF.
# Note: first load may be slow on CPU.
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", grouped_entities=True)


def extract_entities(text: str):
    start = time.time()
    ents = ner(text)
    latency = time.time() - start
    # Naive category: extend with a classifier later
    category = "news" if any('company' in e.get('word','').lower() for e in ents) else "other"
    return {
        "entities": ents,
        "category": category,
        "meta": {"chars": len(text), "latency_s": latency}
    }


def health_check():
    return {"status": "ok"}, 200