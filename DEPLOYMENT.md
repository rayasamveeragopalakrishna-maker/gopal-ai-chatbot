# 🚀 Deployment Guide - Hugging Face Spaces

## Option 1: Deploy with Local Ollama (For Testing)

If you're running Ollama locally and want to test:
1. Push this code to your GitHub repo
2. Create a Hugging Face Space with Streamlit
3. The app will try to connect to `http://localhost:11434`

**Note:** This won't work in Hugging Face Cloud because Ollama isn't installed there.

---

## Option 2: Deploy with Remote Ollama Server (Recommended)

For production, you need Ollama running somewhere accessible.

### Steps:

1. **Host Ollama Remotely** (choose one):
   - Option A: Run on your local machine and expose via ngrok: `ngrok http 11434`
   - Option B: Deploy Ollama on a cloud server (AWS, DigitalOcean, etc.)
   - Option C: Use an Ollama hosting service

2. **Create Hugging Face Space**:
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Select "Streamlit" as SDK
   - Connect your GitHub repo

3. **Set Environment Variables**:
   - In Hugging Face Space settings, add:
     - `OLLAMA_BASE_URL` = your remote URL (e.g., `http://your-server:11434`)
     - `OLLAMA_MODEL` = `llama3.2` (or your choice)

4. **Space auto-deploys** your Streamlit app!

---

## Option 3: Use Hugging Face Inference API (No Ollama Needed)

Modify the app to use Hugging Face's free inference API instead:
- No local Ollama required
- Limited free tier available
- Contact developer for help

---

## Quick Deploy Checklist

- ✅ Code is on GitHub
- ✅ `requirements.txt` is updated
- ✅ `.streamlit/config.toml` created
- ⏳ Next: Create Hugging Face Space & set env vars
