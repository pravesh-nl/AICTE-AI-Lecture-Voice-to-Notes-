import streamlit as st
import google.generativeai as genai
import json
import os
from datetime import datetime
import base64
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from io import BytesIO

st.set_page_config(
    page_title="Your App Name",
    layout="wide",
    initial_sidebar_state="expanded"  # 👈 This makes sidebar open by default
)

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Lecture Voice-to-Notes AI",
    page_icon="🎙",
    layout="wide"
)

# ==========================================
# 🔐 USER ENTERS GEMINI API KEY
# ==========================================
st.sidebar.title("🔐 Gemini API Setup")
user_api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

if not user_api_key:
    st.sidebar.warning("Please enter your Gemini API key to use the app.")
    st.stop()

try:
    genai.configure(api_key=user_api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    st.error(f"Invalid API Key: {e}")
    st.stop()

# ==========================================
# PDF GENERATOR FUNCTION (NEW)
# ==========================================
def generate_pdf(content_text):
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from io import BytesIO
    import html

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]

    for line in content_text.split("\n"):
        safe_line = html.escape(line)   # 🔥 prevents crash
        elements.append(Paragraph(safe_line, normal_style))
        elements.append(Spacer(1, 6))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# ==========================================
# SIMPLE PROFESSIONAL UI
# ==========================================
st.markdown("""
<style>
.stApp { background-color: #0b1f3a; }

div[data-testid="stMarkdownContainer"] p,
div[data-testid="stMarkdownContainer"] li,
div[data-testid="stMarkdownContainer"] span,
label { color: white !important; }

h1, h2, h3, h4, h5, h6 { color: white !important; }

code {
    background-color: #132a4d !important;
    color: #ffcc00 !important;
    padding: 4px 6px;
    border-radius: 6px;
}

section[data-testid="stFileUploader"] {
    background-color: #132a4d !important;
    border: 2px dashed #1f3c88 !important;
    border-radius: 12px;
    padding: 20px;
}

section[data-testid="stFileUploader"] * {
    color: white !important;
    opacity: 1 !important;
}

section[data-testid="stFileUploader"] button {
    background-color: #ffcc00 !important;
    color: black !important;
    border-radius: 8px;
    font-weight: 600;
    border: none;
}

input, textarea {
    background-color: #132a4d !important;
    color: white !important;
}

.stButton>button {
    background-color: #ffcc00;
    color: black !important;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-weight: 600;
    border: none;
}

.stButton>button:hover {
    background-color: #ffd84d;
}

/* Sidebar */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div:first-child {
    background-color: #87CEEB !important;
}

[data-testid="stSidebar"] * {
    color: black !important;
}

[data-testid="stSidebar"] input {
    background-color: white !important;
    color: black !important;
    border-radius: 8px !important;
}

[data-testid="stSidebar"] svg {
    fill: black !important;
}

/* Download button full styling */
div[data-testid="stDownloadButton"] button {
    background-color: #ffcc00 !important;   /* Yellow background */
    color: red !important;                  /* RED text always visible */
    font-weight: 700 !important;
    border-radius: 8px !important;
    border: none !important;
}

/* Hover state */
div[data-testid="stDownloadButton"] button:hover {
    background-color: #ffd84d !important;
    color: darkred !important;
}

/* Uploaded filename */
div[data-testid="stFileUploaderFileName"],
div[data-testid="stFileUploaderFileName"] span {
    color: #ffcc00 !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)
# ==========================================
# HISTORY SETUP
# ==========================================
HISTORY_FILE = "history.json"

if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

def save_history(entry):
    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)
    data.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_history():
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def delete_entry(index):
    data = load_history()
    data.pop(index)
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ==========================================
# MAIN TABS
# ==========================================
tab1, tab2, tab3 = st.tabs(
    ["🎙 Generate Notes", "📂 Previous Works", "🧠 About"]
)

# ==========================================
# TAB 1 — GENERATE NOTES
# ==========================================
with tab1:

    st.title("🎙 Lecture Voice-to-Notes Generator")
    st.divider()

    st.subheader("Upload Audio File")
    audio_file = st.file_uploader("Upload .mp3, .wav, .m4a", type=["mp3", "wav", "m4a"])

    st.divider()

    mcq_count = st.slider("Number of MCQs", 3, 15, 5)
    difficulty = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])

    generate_btn = st.button("🚀 Generate Study Content")

    if generate_btn:

        if not audio_file:
            st.warning("Please upload an audio file.")
            st.stop()

        with st.spinner("Processing..."):

            audio_bytes = audio_file.read()
            mime_type = audio_file.type if audio_file.type else "audio/mp3"

            try:
                encoded_audio = base64.b64encode(audio_bytes).decode("utf-8")

                response = model.generate_content(
                    [
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": """
Transcribe this lecture clearly.

Rules:
- If spoken language is Hindi, convert it into Hinglish.
- If English, keep it in English.
- Do not use Devanagari script.
"""
                                },
                                {
                                    "inline_data": {
                                        "mime_type": mime_type,
                                        "data": encoded_audio
                                    }
                                }
                            ]
                        }
                    ]
                )

                transcript_text = response.text

                result = model.generate_content(
                    f"""
Based on this lecture transcript:

{transcript_text}

IMPORTANT:
- Generate ALL content strictly in English.
- Keep explanations academic and structured.

Provide:

1. Short Summary
2. Detailed Study Notes
3. {mcq_count} {difficulty} MCQs with answers
4. Flashcards
5. Key Concepts
"""
                )

            except Exception as e:
                st.error(f"Processing failed: {e}")
                st.stop()

            st.success("✅ Study Material Generated Successfully!")

            t1, t2 = st.tabs(["📜 Transcript", "📘 Study Content"])

            with t1:
                st.write(transcript_text)

            with t2:
                st.write(result.text)

                # 🔥 NEW PDF DOWNLOAD BUTTON
                pdf_file = generate_pdf(result.text)

                st.download_button(
                    label="📥 Download as PDF",
                    data=pdf_file,
                    file_name="Study_Content.pdf",
                    mime="application/pdf"
                )

            save_history({
                "title": transcript_text[:50],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "content": result.text
            })

# ==========================================
# TAB 2 — HISTORY
# ==========================================
with tab2:

    st.title("📂 Previous Generated Works")
    st.divider()

    history = load_history()

    if history:
        for i, item in enumerate(reversed(history)):
            with st.expander(f"{item['title']} ({item['timestamp']})"):
                st.write(item["content"])
                if st.button("Delete", key=i):
                    delete_entry(len(history) - 1 - i)
                    st.rerun()
    else:
        st.info("No previous works yet.")

# ==========================================
# TAB 3 — ABOUT
# ==========================================
with tab3:

    st.title("🧠 About This Project")
    st.divider()

    st.markdown("""
AI-powered Lecture Voice-to-Notes Generator.

Features:
• Audio Transcription  
• Hindi → Hinglish Transcript Conversion  
• English Study Material  
• Summary  
• Detailed Notes  
• MCQs  
• Flashcards  
• Persistent History  
• PDF Download  

Built using:
• Python  
• Streamlit  
• Google gemini-2.5-flash  
""")