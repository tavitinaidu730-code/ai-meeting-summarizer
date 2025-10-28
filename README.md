🧠 AI Meeting Summarizer + Email Generator
📄 Project Documentation
🔍 Overview

The AI Meeting Summarizer + Email Generator is a Streamlit-based web application powered by Google Gemini AI.
It allows users to:

Upload a meeting transcript (.txt file)

Automatically generate a concise summary of the discussion

Create a professional follow-up email to share with participants

Download all outputs (transcript, summary, and email) as a single text file

This tool helps save time by converting long meeting transcripts into ready-to-share summaries and follow-up emails instantly.

🏗️ Tech Stack
Component	Technology Used
Frontend UI	Streamlit
Backend Logic	Python
AI Model	Google Gemini (via google-generativeai package)
Hosting	Render
Version Control	Git + GitHub
Language	Python 3.10+
⚙️ System Requirements

Python: 3.10 or higher

Libraries:

pip install streamlit google-generativeai python-dotenv


API Key: A valid GOOGLE_API_KEY from Google AI Studio

📁 Project Structure
AI_Meeting_Summarizer/
│
├── app.py                     # Main Streamlit application
├── requirements.txt            # Required Python libraries
├── company_logo.png            # Company logo for header
├── sample_transcript.txt       # (Optional) Sample transcript for testing
├── .env                        # Contains GOOGLE_API_KEY (not committed to GitHub)
└── README.md                   # Documentation file

💡 Features

✅ Upload meeting transcript (TXT file)
✅ Auto-summarization using Gemini AI
✅ Auto generation of professional email draft
✅ Separate output blocks for Summary and Email
✅ Transcript preview before generation
✅ Download button for complete report
✅ Modern layout (logo + title side by side, clean styling)
✅ Works on mobile & desktop

🧩 Code Flow Explanation
1️⃣ Import Required Modules
import streamlit as st
import google.generativeai as genai
import os

2️⃣ Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

3️⃣ Build Streamlit Layout

Two columns at top: logo + title

File uploader to select transcript

Display uploaded transcript

4️⃣ AI Logic (Two Calls to Gemini)

First call: Generates concise summary

Second call: Generates email draft

summary_prompt = "Summarize transcript in 100–150 words..."
email_prompt = "Generate a follow-up email with subject, greeting, action items..."

5️⃣ Display Results

Two side-by-side boxes for Summary and Email

“Download” button for full output

🌐 Deployment on Render
Step 1: Push Code to GitHub
git init
git add .
git commit -m "Initial Commit - AI Meeting Summarizer"
git remote add origin https://github.com/yourusername/ai-meeting-summarizer.git
git push -u origin main

Step 2: Create a Render Web Service

Go to Render Dashboard

Click “New Web Service” → “Connect to GitHub”

Select your repo

Fill the following:

Build Command:

pip install -r requirements.txt


Start Command:

streamlit run app.py --server.port=$PORT --server.address=0.0.0.0


Environment Variable:

Key: GOOGLE_API_KEY
Value: <Your Gemini API Key>


Deploy and wait for build completion.

🧾 Example Output

Uploaded Transcript:

Discussed new client onboarding timeline, assigned John to prepare documentation, reviewed AWS migration progress, and finalized next meeting for Monday.

Summary Block:

The team discussed onboarding progress for the new client. John was assigned to complete the documentation by Friday. AWS migration is on track, and the next meeting is scheduled for Monday to finalize environment testing.

Email Draft Block:

Subject: Follow-up: Client Onboarding and AWS Migration

Hi Team,

Thank you for today’s productive discussion. Below are the agreed action points:

John: Complete client onboarding documentation by Friday.

Priya: Verify AWS environment readiness before Monday.

Next meeting: Monday at 10 AM.

Best,
Manger
