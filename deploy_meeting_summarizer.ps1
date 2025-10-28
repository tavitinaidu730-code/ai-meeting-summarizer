# ============================================
# PowerShell Script: deploy_meeting_summarizer.ps1
# Description:
# 1. Connect to AWS EC2 (Ubuntu)
# 2. Upload project folder
# 3. Open SSH session
# ============================================

# === Step 1: Define variables ===
# Replace with your EC2 public IP address
$EC2_IP = "13.233.126.231"

# Path to your .pem key
$PEM_PATH = "C:\Users\TavitiNaidu\AWSKeys\meeting-summarizer.pem"

# Local project folder path (adjust if needed)
$LOCAL_PROJECT_PATH = "C:\Users\TavitiNaidu\AI_Meeting_Summarizer"

# Remote folder on EC2
$REMOTE_PATH = "/home/ubuntu/AI_Meeting_Summarizer"

Write-Host "==== AWS EC2 Deployment Script ====" -ForegroundColor Cyan
Write-Host "EC2 IP Address : $EC2_IP"
Write-Host "PEM Key Path   : $PEM_PATH"
Write-Host "Local Folder   : $LOCAL_PROJECT_PATH"
Write-Host "====================================="

# === Step 2: Check if the key file exists ===
if (-Not (Test-Path $PEM_PATH)) {
    Write-Host "❌ PEM key not found at $PEM_PATH" -ForegroundColor Red
    exit
}

# === Step 3: Upload local project folder to EC2 ===
Write-Host "📦 Uploading project to EC2..." -ForegroundColor Yellow
scp -i $PEM_PATH -r $LOCAL_PROJECT_PATH "ubuntu@${EC2_IP}:$REMOTE_PATH"

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to upload project." -ForegroundColor Red
    exit
}

Write-Host "✅ Upload completed successfully." -ForegroundColor Green

# === Step 4: Connect to EC2 ===
Write-Host "🔗 Connecting to EC2 instance..." -ForegroundColor Yellow
ssh -i $PEM_PATH "ubuntu@${EC2_IP}"