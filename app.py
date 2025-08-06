from flask import Flask, request, render_template
from pymongo import MongoClient

import subprocess
import os
from PIL import Image
import pytesseract

app = Flask(__name__)

client = MongoClient("mongodb+srv://sv695177:w626TaWXZCBffmDz@cluster0.fcdm5ox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["Siksha_Mitra"]
history_collection = db["conversation_history"]

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

history = []
language = "en"

@app.route('/', methods=['GET', 'POST'])
def home():
    global language
    response = ""
    if request.method == 'POST':
        action = request.form.get("action")
        print(f"[DEBUG] Action received: {action}")

        if action == "text":
            user_input = request.form.get('text_input', '')
            print(f"[DEBUG] Text input: {user_input}")

            # Language switching keywords
            if "bhasha badlo" in user_input.lower() or "change language" in user_input.lower():
                if "hindi" in user_input.lower():
                    language = "hi"
                    response = "✅ भाषा हिंदी में बदल गई है।"
                elif "marathi" in user_input.lower():
                    language = "mr"
                    response = "✅ मराठीमध्ये उत्तर दिलं जाईल."
                elif "gujarati" in user_input.lower():
                    language = "gu"
                    response = "✅ હવે ગુજરાતી ભાષામાં જવાબ મળશે."
                elif "russian" in user_input.lower():
                    language = "ru"
                    response = "✅ Язык переключен на русский."
                elif "english" in user_input.lower():
                    language = "en"
                    response = "✅ Language switched to English."
                elif "bihari" in user_input.lower() or "bhojpuri" in user_input.lower():
                    language = "bho"
                    response = "✅ अब जबाब भोजपुरी में दीहल जाई।"
                else:
                    response = "❌ Language not recognized. Try again."
            else:
                response = query_gemma(user_input)

        elif action == "image":
            image = request.files.get("image")

            if not image or image.filename == '':
                print("[DEBUG] No image file selected")
                response = "Please upload a valid image file."
            else:
                image_path = "temp.jpg"
                image.save(image_path)
                print(f"[DEBUG] Saved uploaded image to {image_path}")

                try:
                    extracted_text = pytesseract.image_to_string(Image.open(image_path)).strip()
                    print(f"[DEBUG] OCR Text: {extracted_text}")

                    if not extracted_text:
                        response = "No readable text found in the image."
                    else:
                        prompt = f"This image contains: {extracted_text}. Please explain this for a 10-year-old."
                        response = query_gemma(prompt)

                except Exception as e:
                    print(f"[ERROR] OCR failed: {e}")
                    response = "Something went wrong while reading the image."

                os.remove(image_path)

    return render_template("index.html", response=response)

def save_history(user_id, question, answer):
    history_collection.insert_one({
        "user": user_id,
        "question": question,
        "answer": answer
    })

def get_recent_history(user_id, limit=5):
    docs = history_collection.find({"user": user_id}).sort("_id", -1).limit(limit)
    return [f"User: {doc['question']}\nGemma: {doc['answer']}" for doc in reversed(list(docs))]

def query_gemma(user_input, user_id="user1"):
    past_context = "\n".join(get_recent_history(user_id))

    lang_instruction = {
        "en": "",
        "hi": "Translate the answer to Hindi.\n",
        "mr": "Translate the answer to Marathi.\n",
        "gu": "Translate the answer to Gujarati.\n",
        "ru": "Translate the answer to Russian.\n",
        "bho": "Translate the answer to Bhojpuri.\n"
    }.get(language, "")

    prompt = (
        "You are a helpful offline tutor. Always give structured answers:\n"
        "Start with a 1-2 line explanation.\n"
        "Then list the steps or key points clearly.\n"
        "Use simple language for children.\n\n"
        f"{lang_instruction}"
        f"{past_context}\nUser: {user_input}"
    )

    try:
        result = subprocess.run(
            ["C:\\Users\\acer\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "run", "gemma:2b"],
            input=prompt.encode(),
            stdout=subprocess.PIPE
        )
        output = result.stdout.decode()
        save_history(user_id, user_input, output)
        return output

    except Exception as e:
        print(f"[ERROR] Ollama call failed: {e}")
        return "Gemma failed to respond."

if __name__ == '__main__':
    app.run(debug=True)
