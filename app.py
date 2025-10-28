import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import base64

# Load environment variables from .env
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Or directly set key if .env not working:
# genai.configure(api_key="AIzaSyCp***************************GOq4")

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit App Title
st.set_page_config(page_title="AI Meeting Summarizer + Email Generator", layout="centered")
st.title("🧠 AI Meeting Summarizer + Email Generator")

st.markdown(
    "Upload a **meeting transcript (.txt)** below. "
    "The tool will generate a **concise summary** and a **draft follow-up email** automatically."
)

# File uploader
uploaded_file = st.file_uploader("📁 Upload meeting transcript", type="txt")

if uploaded_file is not None:
    transcript = uploaded_file.read().decode("utf-8")
    st.subheader("🗒️ Meeting Transcript")
    st.text_area("Transcript:", transcript, height=200)

    if st.button("✨ Generate Summary and Email"):
        with st.spinner("AI is processing your transcript... please wait ⏳"):
            # ---------- Improved Prompt for Summary ----------
            summary_prompt = f"""
You are an expert meeting summarizer.
Read the meeting transcript below and create a concise, professional summary (100–150 words) with:
1. Main agenda or topic
2. Key points discussed
3. Decisions made
4. Action items (who will do what and by when)

Transcript:
{transcript}
"""

            summary_response = model.generate_content(summary_prompt)
            summary = summary_response.text.strip()

            # ---------- Improved Prompt for Email ----------
            email_prompt = f"""
You are a professional assistant helping to write follow-up emails after meetings.
Using the meeting transcript below, create a clear, polite, and action-oriented follow-up email with:
- Subject line
- Greeting
- Key updates & next steps in bullet format
- Call to action if needed
- Polite closing

Avoid repeating words or phrases. Keep tone business-friendly and concise.

Transcript:
{transcript}
"""

            email_response = model.generate_content(email_prompt)
            email = email_response.text.strip()

        # ---------- Display Results ----------
        st.success("✅ Summary and Email Generated Successfully!")

        st.subheader("📝 Meeting Summary")
        st.write(summary)

        st.subheader("✉️ Follow-up Email Draft")
        st.write(email)

        # ---------- Download Buttons ----------
        def download_button(label, text, file_name):
            b64 = base64.b64encode(text.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="{file_name}">{label}</a>'
            st.markdown(href, unsafe_allow_html=True)

        st.markdown("### 📥 Download Options")
        download_button("⬇️ Download Summary", summary, "meeting_summary.txt")
        download_button("⬇️ Download Email", email, "followup_email.txt")

else:
    st.info("👆 Please upload a transcript file to begin.")
