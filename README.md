# ML API: T5 Summarization & GPT-2 Text Generation

A FastAPI application serving two fine‑tuned transformer models:
- **T5** for text summarization
- **GPT‑2** for text generation

Protected by API‑key authentication.  
**Live Demo**: [Hugging Face Space URL] (add later)

## Endpoints
- `POST /summarize` – Summarize text
- `POST /generate` – Generate text
- `GET /docs` – Interactive docs

## Run locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
