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
Built with a custom UI theme, interactive sidebar configuration, and clean deployment-ready architecture.

---

## 🌟 Live Demo

(https://aicte-ai-lecture-voice-to-notes.streamlit.app/)

---

## ✨ Features

- 🧠 AI-powered content generation
- 📄 Download generated content as PDF
- 🎨 Custom styled UI (dark theme + sky blue sidebar)
- 🔐 Secure API key input from sidebar
- 📂 File upload support
- ⚡ Fast and lightweight
- ☁️ Ready for Streamlit Cloud deployment

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit**
- **ReportLab** (PDF generation)
- **OpenAI API**
- HTML + CSS (custom styling inside Streamlit)

---

## 📁 Project Structure


AICTE-Al-Lecture-Voice-to-Notes- /
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── assets # Screenshots


---

## ⚙️ Installation (Run Locally)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the application
streamlit run app.py

The app will open in your browser at:

http://localhost:8501
🔐 API Key Setup

This app requires an OpenAI API key.

You can enter it securely from the sidebar input field when running the app.

⚠️ Never hardcode your API key inside the code.
⚠️ Do not push your .env file to GitHub.

☁️ Deploy on Streamlit Cloud

Push your project to GitHub

Go to: https://share.streamlit.io

Connect your GitHub account

Select repository

Choose app.py as main file

Click Deploy

Your app will be live in minutes 🚀

🎨 UI Customization

The app includes:

Dark blue main background

Sky blue sidebar

Custom styled buttons

Styled file uploader

Highlighted code blocks

Custom red PDF download button

All styling is handled using embedded CSS via:

st.markdown("<style>...</style>", unsafe_allow_html=True)
📄 PDF Download Feature

The application uses ReportLab to generate downloadable PDF files from the generated content.

Features:

Clean formatting

Structured text rendering

One-click download button

🧪 Requirements
streamlit
reportlab
openai
python-dotenv (optional)
🔒 Security Notes

API key is entered securely in sidebar

.env file is ignored using .gitignore

No sensitive data stored in repo

🚀 Future Improvements

Multi-page PDF export

User authentication

History of generated outputs

Database integration

Custom branding options

Animation enhancements

Dark/Light mode toggle

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a new branch

Make improvements

Submit a pull request

📜 License

This project is open-source 
