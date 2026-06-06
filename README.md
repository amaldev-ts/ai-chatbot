# 🤖 AI Chatbot

A beautiful ChatGPT-style AI chatbot with image analysis, file reading, voice input, and more!

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- 💬 **Real-time Chat** — Stream responses like ChatGPT
- 📷 **Image Analysis** — Upload images and ask questions
- 📎 **File Reading** — Supports PDF, DOCX, TXT files
- 🎤 **Voice Input** — Speak instead of typing
- 💾 **Multiple Chats** — Save & switch conversations
- 🔍 **Search Chats** — Find old conversations easily
- ✏️ **Edit/Delete Chats** — Manage your history
- 📋 **Code Blocks** — Beautiful code with copy button
- 🌙 **Dark Theme** — Easy on the eyes

---

## 🖼️ Screenshots

> Add your screenshots here later!

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **AI Model:** Gemini API
- **Frontend:** HTML, CSS, JavaScript
- **Libraries:** Pillow, PyPDF2, python-docx

---

## 📋 Requirements

Before starting, make sure you have:

- ✅ Python 3.10 or higher installed
- ✅ Internet connection
- ✅ Free Gemini API key (we'll get it below)

---

## 🚀 How to Use This Chatbot

### Step 1: Install Python

Download from: https://www.python.org/downloads/

> ⚠️ During install, check **"Add Python to PATH"**

---

### Step 2: Download This Project

**Option A — Using Git:**

```bash
git clone https://github.com/amaldev-ts/ai-chatbot.git
cd ai-chatbot
```

**Option B — Without Git:**

1. Click green **"Code"** button on this page
2. Click **"Download ZIP"**
3. Extract the ZIP file
4. Open the folder

---

### Step 3: Install Required Libraries

Open terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

---

### Step 4: Get FREE Gemini API Key

1. Visit: **https://aistudio.google.com/apikey**
2. Login with your Google account
3. Click **"Create API key"**
4. **Copy** the key (looks like: `AIzaSy...`)

---

### Step 5: Create `.env` File

1. In the project folder, create a new file named `.env`
2. Add this line (paste your key):

```
GEMINI_API_KEY=your_api_key_here
```

3. Save the file

> ⚠️ Replace `your_api_key_here` with your actual API key

---

### Step 6: Run the Chatbot

In terminal, run:

```bash
python app.py
```

You'll see:

```
🤖 AI CHATBOT by AMAL DEV T S - http://127.0.0.1:5000
```

---

### Step 7: Open in Browser

Open your browser and visit:

```
http://127.0.0.1:5000
```

🎉 **Enjoy your AI Chatbot!**

---

## 📁 Project Structure

```
ai-chatbot/
├── app.py              # Main Flask backend
├── requirements.txt    # Python libraries
├── .env                # API key (you create this)
├── .gitignore          # Git ignore rules
├── templates/
│   └── index.html      # Frontend HTML
└── static/
    └── style.css       # Styling
```

---

## 🎯 How to Use Features

### 💬 Text Chat
Just type your message and press **Enter** or click **Send**

### 📷 Image Upload
1. Click the **📷 camera icon**
2. Select an image
3. Type your question (or leave empty)
4. Click **Send**

### 📎 File Upload
1. Click the **📎 clip icon**
2. Select PDF, DOCX, or TXT file
3. Type what you want to know
4. Click **Send**

### 🎤 Voice Input
1. Click the **🎤 microphone icon**
2. Allow microphone permission
3. Speak your message
4. Click **Send**

> **Note:** Voice works only in Chrome, Edge, or Brave browsers

### 💾 Manage Chats
- **New Chat:** Click **"+ New Chat"** in sidebar
- **Rename:** Hover over chat → Click **✏️**
- **Delete:** Hover over chat → Click **🗑️**
- **Search:** Use search box in sidebar

---

## 🆘 Troubleshooting

### ❌ Error: `pip is not recognized`
**Fix:** Use `python -m pip install -r requirements.txt`

### ❌ Error: `Module not found`
**Fix:** Run `pip install -r requirements.txt` again

### ❌ Error: `API key invalid`
**Fix:** Check your `.env` file has correct key

### ❌ Error: `429 Quota exceeded`
**Fix:** Wait 1 minute (free tier limit)

### ❌ Voice not working
**Fix:** Use Chrome/Edge/Brave + allow microphone

---

## 📋 requirements.txt

If missing, create `requirements.txt` with this content:

```
flask
google-generativeai
python-dotenv
Pillow
PyPDF2
python-docx
```

---

## 🌟 Show Your Support

If you like this project:
- ⭐ Star this repo
- 🍴 Fork and customize it
- 📢 Share with others

---

## 👨‍💻 Developer

**AMAL DEV T S**

- GitHub: [@amaldev-ts](https://github.com/amaldev-ts)
- Email: amalts5885@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Built with ❤️ by Amal Dev T S
- Powered by Gemini AI
- Inspired by ChatGPT

---

⭐ **Don't forget to star this repo if you find it useful!**
