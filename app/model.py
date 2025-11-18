from transformers import pipeline
import time
import os

# Disable TensorFlow warnings and force PyTorch
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# small grouped-entities NER pipeline for dev. Replace model with anything from HF.
# Note: first load may be slow on CPU. Using PyTorch framework explicitly.
# Using a more reliable model that's always available
ner = pipeline("ner", 
               model="dslim/bert-base-NER", 
               aggregation_strategy="simple",
               framework="pt")  # Force PyTorch


def extract_entities(text: str):
    start = time.time()
    ents = ner(text)
    latency = time.time() - start
    
    # Convert numpy types to Python native types for JSON serialization
    processed_ents = []
    for entity in ents:
        processed_entity = {
            "entity_group": entity.get("entity_group"),
            "score": float(entity.get("score", 0)),  # Convert numpy.float32 to float
            "word": entity.get("word"),
            "start": int(entity.get("start", 0)),    # Convert numpy.int64 to int
            "end": int(entity.get("end", 0))         # Convert numpy.int64 to int
        }
        processed_ents.append(processed_entity)
    
    # Naive category: extend with a classifier later
    # Check for organization entities to categorize as news
    category = "other"
    try:
        for entity in processed_ents:
            if entity.get('entity_group') == 'ORG' or 'company' in entity.get('word', '').lower():
                category = "news"
                break
    except Exception:
        category = "other"
    
    return {
        "entities": processed_ents,
        "category": category,
        "meta": {"chars": len(text), "latency_s": latency}
    }


def health_check():
    return {"status": "ok"}