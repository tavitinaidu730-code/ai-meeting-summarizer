import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit page setup
st.set_page_config(
    page_title="AI Meeting Summarizer + Email Generator",
    page_icon="🧠",
    layout="wide"
)

# --- Header Section: Logo + Title Side by Side ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image("company_logo.png", width=200)  # 👈 Put your logo file here or use a URL
with col2:
    st.markdown(
        """
        <div style='display: flex; align-items: center; height: 100%;'>
            <h1 style='margin: 0; padding-left: 10px;'>AI Meeting Summarizer + Email Generator</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# --- File Upload Section ---
uploaded_file = st.file_uploader("📤 Upload your meeting transcript (.txt)", type=["txt"])

if uploaded_file is not None:
    transcript = uploaded_file.read().decode("utf-8")

    # --- Show Transcript Preview ---
    st.markdown("### 📄 Uploaded Transcript")
    st.markdown(
        f"<div style='background-color:#F9FAFB;padding:15px;border-radius:10px;border:1px solid #ddd;max-height:300px;overflow-y:auto;white-space:pre-wrap;'>{transcript}</div>",
        unsafe_allow_html=True
    )

    # --- Generate AI Summary and Email Draft ---
    with st.spinner("🧠 Generating summary and follow-up email... please wait..."):
        prompt = f"""
        You are an expert meeting summarizer and email writer.
        Given the meeting transcript below, generate:
        A professional meeting summary (100–150 words)
        A well-formatted follow-up email draft with clear next steps.

        Transcript:
        {transcript}
        """

        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

    # --- Layout for Output ---
    st.markdown("### 📝 Summary and Email Draft")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧾 Meeting Summary")
        st.markdown(
            f"<div style='background-color:#F7F9FC;padding:15px;border-radius:10px;border:1px solid #ccc;'>{response.text.split('Follow-up Email')[0]}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.subheader("📧 Follow-up Email Draft")
        st.markdown(
            f"<div style='background-color:#F7FFF7;padding:15px;border-radius:10px;border:1px solid #ccc;'>{response.text.split('Follow-up Email')[-1]}</div>",
            unsafe_allow_html=True
        )

    # --- Download Button ---
    download_text = f"Meeting Transcript:\n\n{transcript}\n\n{response.text}"
    st.download_button(
        label="⬇️ Download Summary & Email",
        data=download_text,
        file_name="meeting_summary_email.txt",
        mime="text/plain"
    )

else:
    st.info("📄 Please upload a meeting transcript file to generate summary and email.")
