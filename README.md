

# 🧠 Medical ChatBot – AI Assistant for Medical Documents

This project is an **AI-powered medical chatbot** that intelligently reads and understands medical PDF documents to answer user queries in natural language. Whether it's a research paper, clinical guideline, or patient report, the chatbot extracts relevant insights and provides conversational answers with context awareness.

---

## 🚀 Features

- 📄 **PDF Understanding** – Parses and processes uploaded medical documents.
- 🔍 **Contextual Q&A** – Asks questions and receives answers based on document content.
- 🤖 **LLM-Driven** – Utilizes Google's `flan-t5-large` model via Hugging Face Hub.
- 🧠 **Memory-Aware** – Maintains chat history using LangChain's memory module.
- 💬 **Gradio Interface** – Interactive web-based chat UI, no technical setup needed.

---

## 📁 Files Included

```
├── app.py                # Gradio application with LangChain logic
├── requirements.txt      # All Python dependencies
├── sample.pdf            # A dummy PDF document for testing
├── README.md             # Project overview and instructions
```

---

## 📦 Installation & Deployment (on Hugging Face Spaces)

1. **Upload all project files** to your Hugging Face Space.
2. **Add your Hugging Face API token** under Settings → Secrets:
   ```
   Name: HUGGINGFACEHUB_API_TOKEN
   Value: your_hf_token_here
   ```
3. The app will auto-launch with Gradio and serve the chatbot interface.

---

## 💡 Example Use Cases

- 🏥 Doctors: "What does the discharge summary say about medications?"
- 👨‍⚕️ Pharmacists: "What are the listed side effects in this report?"
- 🧪 Researchers: "Summarize the methodology section of this paper."

---

## 🧰 Built With

- [LangChain](https://python.langchain.com/)
- [Gradio](https://gradio.app/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Hugging Face Transformers](https://huggingface.co/)

---

## 👨‍💻 Author

Developed by **Aditya Yadav**  
🎓 CSE @ MMMUT | 🛠️ AI/ML Developer | 🚀 DST Project Associate

---

## 📬 Get in Touch

For collaborations, improvements, or support:  
📧 [LinkedIn](https://www.linkedin.com/in/aditya-ai)

---

> ⚠️ Disclaimer: This chatbot is for demonstration/educational purposes. It is not intended for real-time medical diagnosis or treatment.
