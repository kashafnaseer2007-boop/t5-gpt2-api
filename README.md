# 🚀 ML API: T5 Summarization & GPT-2 Text Generation

A **FastAPI application** serving two fine-tuned transformer models:

- ✨ **T5** → Text Summarization  
- 🤖 **GPT-2** → Text Generation  

🔐 Secured with **API-key authentication**

> 🌐 **Live Demo**: *(Add your Hugging Face Space URL here)*

---

## 📌 Features

- Fast and efficient API built with **FastAPI**
- Fine-tuned transformer models using **Hugging Face Transformers**
- Secure access with API key authentication
- Ready for deployment with Docker

---

## 📡 API Endpoints

| Method | Endpoint        | Description              |
|--------|----------------|--------------------------|
| POST   | `/summarize`   | Summarize input text     |
| POST   | `/generate`    | Generate text            |
| GET    | `/docs`        | Interactive API docs     |

---

## ⚙️ Run Locally

```bash
# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

---

## 📁 Project Structure

```
.
├── main.py                # FastAPI application
├── keys.py                # API key configuration (local only)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Deployment configuration (Hugging Face Spaces)
├── .gitignore             # Ignored files
├── README.md              # Project documentation
└── models/
    ├── t5_summarization/  # Fine-tuned T5 model
    └── gpt2_textgen/      # Fine-tuned GPT-2 model
```

---

## 🧠 Training Notebooks

Want to see how these models were trained?  
You can explore and run the notebooks for free on Kaggle:

- 📄 **T5 Summarization Notebook**  
  https://www.kaggle.com/code/kashafrana2007/summarization-with-t5  

- 📄 **GPT-2 Text Generation Notebook**  
  https://www.kaggle.com/code/kashafrana2007/text-generation-with-gpt2  

---

## 🔍 What’s Inside the Notebooks?

- Step-by-step fine-tuning using **Hugging Face Transformers**
- Dataset loading & preprocessing
- Training configurations & loss tracking
- Model saving for deployment

---

## 🤝 Contributing / Learning

Feel free to **fork**, modify, and experiment with this project.  
No need to start from scratch — everything is structured to help you learn quickly 🚀
