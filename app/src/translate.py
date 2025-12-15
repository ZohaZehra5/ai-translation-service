from functools import lru_cache
from transformers import pipeline
from .languages import SUPPORTED_TRANSLATIONS

@lru_cache(maxsize=5)
def load_model(model_name: str):
    return pipeline("translation", model=model_name)

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    key = (source_lang, target_lang)

    if key not in SUPPORTED_TRANSLATIONS:
        raise ValueError(f"Unsupported translation: {source_lang} -> {target_lang}")

    model = load_model(SUPPORTED_TRANSLATIONS[key])
    output = model(text, max_length=256)

    return output[0]["translation_text"]
