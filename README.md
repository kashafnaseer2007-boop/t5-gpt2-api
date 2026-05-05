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

## Project Structure
├── main.py # FastAPI application
├── keys.py # API key configuration (local only)
├── requirements.txt # Python dependencies
├── Dockerfile # Deployment configuration for Hugging Face Spaces
├── .gitignore # Files and folders to ignore
├── README.md # Project documentation
└── models/
├── t5_summarization/ # Fine-tuned T5 model for summarization
└── gpt2_textgen/ # Fine-tuned GPT-2 model for text generation

## 📓 Training Notebooks
Want to see how these models were trained?  
You can open and run the original notebooks for free on Kaggle:

- **T5 Summarization** – [fine_tune_t5_summarization.ipynb]([https://www.kaggle.com/code/your-username/your-t5-notebook](https://www.kaggle.com/code/kashafrana2007/summarization-with-t5))
- **GPT‑2 Text Generation** – [fine_tune_gpt2_textgen.ipynb]([https://www.kaggle.com/code/your-username/your-gpt2-notebook](https://www.kaggle.com/code/kashafrana2007/text-generation-with-gpt2))

### 🧪 What’s inside?
- Step‑by‑step fine‑tuning with Hugging Face Transformers
- Dataset loading & preprocessing
- Training arguments & loss curves
- Saving the model for deployment

Feel free to fork, change, and learn from them — no need to start from scratch.
