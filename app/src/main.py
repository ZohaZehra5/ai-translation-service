from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .translate import translate_text

app = FastAPI(title="AI Translation Service")

class TranslateRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/translate")
def translate(req: TranslateRequest):
    try:
        result = translate_text(req.text, req.source_lang, req.target_lang)
        return {
            "source_lang": req.source_lang,
            "target_lang": req.target_lang,
            "translation": result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
