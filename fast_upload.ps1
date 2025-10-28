# ==========================================
#  FAST AWS UPLOAD SCRIPT FOR STREAMLIT APP
# ==========================================

# --- CONFIGURATION ---
$PEM_PATH = "C:\Users\TavitiNaidu\AWSKeys\meeting-summarizer.pem"
$LOCAL_PATH = "C:\Users\TavitiNaidu\AI_Meeting_Summarizer"
$EC2_IP = "13.233.126.231"
$REMOTE_PATH = "/home/ubuntu/AI_Meeting_Summarizer"

Write-Host "==== Fast Upload to EC2 Started ====" -ForegroundColor Cyan
Write-Host "Uploading only essential app files..." -ForegroundColor Yellow

# --- STEP 1: Create remote folder if not exists ---
ssh -i "$PEM_PATH" ubuntu@$EC2_IP "mkdir -p $REMOTE_PATH"

# --- STEP 2: Upload main app files ---
scp -i "$PEM_PATH" `
    "$LOCAL_PATH\app.py" `
    "$LOCAL_PATH\summary_utils.py" `
    "$LOCAL_PATH\requirements.txt" `
    "ubuntu@${EC2_IP}:${REMOTE_PATH}/"

# --- STEP 3: Upload folders ---
scp -i "$PEM_PATH" -r `
    "$LOCAL_PATH\templates" `
    "$LOCAL_PATH\static" `
    "ubuntu@${EC2_IP}:${REMOTE_PATH}/"

Write-Host "✅ Upload completed successfully!" -ForegroundColor Green
Write-Host "You can now SSH into EC2 and run the app." -ForegroundColor Cyan
Write-Host "Command: ssh -i `"$PEM_PATH`" ubuntu@$EC2_IP"
