from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer, GPT2LMHeadModel, GPT2Tokenizer
import torch
from os

API_KEY = os.getenv("API_KEY", "supersecret123")

app = FastAPI(title="T5 Summarization & GPT-2 Text Generation API",
              description="A secure ML API serving fine-tuned T5 and GPT-2 models. Built with FastAPI + Hugging Face Transformers.",
              version="1.0.0")

# ---------- API Key Guard ----------
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def verify_api_key(key: str = Depends(api_key_header)):
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return key

# ---------- Load Models ----------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# T5
t5_model = T5ForConditionalGeneration.from_pretrained("models/t5_summarization").to(device)
t5_tokenizer = T5Tokenizer.from_pretrained("models/t5_summarization")

# GPT-2
gpt2_model = GPT2LMHeadModel.from_pretrained("models/gpt2_textgen").to(device)
gpt2_tokenizer = GPT2Tokenizer.from_pretrained("models/gpt2_textgen")
gpt2_tokenizer.pad_token = gpt2_tokenizer.eos_token

# ---------- Input Shapes ----------
class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 150

class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 100

# ---------- Endpoints ----------
@app.get("/")
def root():
    return {"message": "ML API is running! Use /docs to test."}

@app.post("/summarize")
def summarize(req: SummarizeRequest, api_key: str = Depends(verify_api_key)):
    input_text = "summarize: " + req.text
    inputs = t5_tokenizer.encode(input_text, return_tensors="pt", truncation=True).to(device)
    summary_ids = t5_model.generate(inputs, max_length=req.max_length, num_beams=4, early_stopping=True)
    summary = t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return {"summary": summary}

@app.post("/generate")
def generate(req: GenerateRequest, api_key: str = Depends(verify_api_key)):
    inputs = gpt2_tokenizer.encode(req.prompt, return_tensors="pt").to(device)
    output = gpt2_model.generate(
        inputs,
        max_length=req.max_length,
        do_sample=True,
        temperature=0.7,
        pad_token_id=gpt2_tokenizer.eos_token_id
    )
    generated = gpt2_tokenizer.decode(output[0], skip_special_tokens=True)
    return {"generated_text": generated}