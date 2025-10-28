# 🧠 AI Meeting Summarizer + Email Generator

This tool reads a meeting transcript (text file) and generates:
- A short summary (100–150 words)
- A draft follow-up email with action points

## 🚀 How to Run

### 1️⃣ Install Python & Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Add OpenAI API Key
Create a file named `.env` and paste your API key:
```
OPENAI_API_KEY=your_api_key_here
```

### 3️⃣ Run the App
```bash
streamlit run app.py
```

### 4️⃣ Open in Browser
It will open at: `http://localhost:8501`

Upload any `.txt` transcript file → get Summary → Email.

---

✅ Technologies Used:
- Python
- Streamlit
- OpenAI API
- dotenv

Enjoy building! 🚀
