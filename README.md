# AICTE-AI-Lecture-Voice-to-Notes-
# 🎤 AI Voice to Study Notes Generator

An AI-powered Streamlit web application that converts voice or input content into structured, clean, and easy-to-read study notes — with instant PDF download support.

Designed for students who want quick revision material from lectures, recordings, or spoken input.

---

## 🌟 What This App Does

- 🎙 Convert voice/lecture input into structured notes
- 🧠 AI-powered summarization and formatting
- 📚 Generates clean study material
- 📄 Download notes as PDF
- 🎨 Modern custom UI (dark theme + styled sidebar)
- 🔐 Secure API key input

---

## ✨ Features

- Voice → Notes conversion
- AI-based summarization
- Bullet-point structured notes
- Highlighted important points
- One-click PDF export
- Deployment-ready architecture
- Clean and responsive UI

---

## 🛠 Tech Stack

- Python 3.9+
- Streamlit
- OpenAI API
- ReportLab (PDF generation)
- Custom CSS styling

---

## 📁 Project Structure


ai-voice-notes-generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Run Locally

### 1️⃣ Clone Repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Start App
streamlit run app.py
🔐 API Key Setup

Enter your OpenAI API key securely from the sidebar.

⚠️ Do not hardcode API keys
⚠️ Do not push .env file to GitHub

📄 PDF Export

Generated notes can be downloaded as a structured PDF file using ReportLab.
