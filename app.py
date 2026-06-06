from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import PyPDF2
import docx
import os
import json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    "models/gemini-flash-latest",
    system_instruction=(
        "You are 'AI Chatbot', created by Amal Dev T S. "
        "Never mention Google, Gemini, or any company. "
        "If asked who made you, say: 'I was created by Amal Dev T S.' "
        "Be friendly and use markdown formatting with code blocks when sharing code."
    )
)

# Store multiple chat sessions
chat_sessions = {}

def get_or_create_chat(chat_id):
    if chat_id not in chat_sessions:
        chat_sessions[chat_id] = model.start_chat(history=[])
    return chat_sessions[chat_id]

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_IMAGE_EXT = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
ALLOWED_FILE_EXT = {'pdf', 'txt', 'docx'}

def allowed_file(filename, allowed_set):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set

def extract_text_from_pdf(file):
    try:
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages])
    except Exception as e:
        return f"Error: {str(e)}"

def extract_text_from_docx(file):
    try:
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat-stream", methods=["POST"])
def chat_stream():
    """Streaming response for fast typing effect"""
    data = request.json
    user_message = data.get("message", "")
    chat_id = data.get("chat_id", "default")
    
    chat = get_or_create_chat(chat_id)
    
    def generate():
        try:
            response = chat.send_message(user_message, stream=True)
            for chunk in response:
                if chunk.text:
                    yield f"data: {json.dumps({'text': chunk.text})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"
        except Exception as e:
            err = str(e)
            if "429" in err:
                yield f"data: {json.dumps({'text': '⏱️ Too many requests! Please wait.', 'done': True})}\n\n"
            else:
                yield f"data: {json.dumps({'text': '❌ Error occurred.', 'done': True})}\n\n"
    
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

@app.route("/upload-image", methods=["POST"])
def upload_image():
    try:
        file = request.files.get('image')
        user_text = request.form.get('message', 'What is in this image?')
        chat_id = request.form.get('chat_id', 'default')
        
        if not file or not allowed_file(file.filename, ALLOWED_IMAGE_EXT):
            return jsonify({"reply": "❌ Invalid image"})
        
        image = Image.open(file.stream)
        response = model.generate_content([user_text, image])
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"❌ Error: {str(e)}"})

@app.route("/upload-file", methods=["POST"])
def upload_file():
    try:
        file = request.files.get('file')
        user_text = request.form.get('message', 'Summarize this document')
        chat_id = request.form.get('chat_id', 'default')
        
        if not file or not allowed_file(file.filename, ALLOWED_FILE_EXT):
            return jsonify({"reply": "❌ Invalid file"})
        
        ext = file.filename.rsplit('.', 1)[1].lower()
        if ext == 'pdf':
            text = extract_text_from_pdf(file)
        elif ext == 'docx':
            text = extract_text_from_docx(file)
        else:
            text = file.read().decode('utf-8', errors='ignore')
        
        if len(text) > 30000:
            text = text[:30000] + "\n...(truncated)"
        
        chat = get_or_create_chat(chat_id)
        response = chat.send_message(f"{user_text}\n\nDocument:\n{text}")
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"❌ Error: {str(e)}"})

@app.route("/reset", methods=["POST"])
def reset_chat():
    chat_id = request.json.get("chat_id", "default")
    if chat_id in chat_sessions:
        del chat_sessions[chat_id]
    return jsonify({"status": "success"})

if __name__ == "__main__":
    print("\n🤖 AI CHATBOT by AMAL DEV T S - http://127.0.0.1:5000\n")
    app.run(debug=True, threaded=True)