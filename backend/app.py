from flask import Flask, request, jsonify
import subprocess
import openai
import base64
import os
from flask_cors import CORS
from dotenv import load_dotenv

# ---------------- Load environment variables ---------------- #
load_dotenv()  # loads from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# ---------------- Flask Setup ---------------- #
app = Flask(__name__)
CORS(app)
language = "en"

# Ollama models
PREFERRED_MODEL = "gemma:7b"
FALLBACK_MODEL = "gemma:2b"

# ---------------- Helper Functions ---------------- #
def generate_image(prompt):
    os.makedirs("static", exist_ok=True)
    output_path = os.path.join("static", f"{prompt[:10].replace(' ','_')}.png")
    try:
        response = openai.images.generate(
            prompt=prompt,
            size="1024x1024"
        )
        image_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)
        with open(output_path, "wb") as f:
            f.write(image_bytes)
        return output_path
    except Exception as e:
        print(f"Image generation failed: {e}")
        return None

def switch_language(user_input):
    global language
    mapping = {
        "hindi": "hi", "marathi": "mr", "gujarati": "gu",
        "russian": "ru", "english": "en", "bihari": "bho", "bhojpuri": "bho"
    }
    for key, val in mapping.items():
        if key in user_input.lower():
            language = val
            return f"Language switched to {key.capitalize()}."
    return "Language not recognized."

def query_gemma(user_input):
    prompt = f"""
You are a helpful AI tutor. Answer naturally, but include short inline references from standard textbooks or commonly known sources whenever explaining factual information.
Keep it simple, friendly, and engaging.
User: {user_input}
"""
    OLLAMA_PATH = os.environ.get("OLLAMA_PATH", "ollama")

    for model in [PREFERRED_MODEL, FALLBACK_MODEL]:
        try:
            result = subprocess.run(
                [OLLAMA_PATH, "run", model],
                input=prompt.encode(),
                stdout=subprocess.PIPE,
                timeout=30
            )
            output = result.stdout.decode().strip()
            if output:
                return output
        except Exception as e:
            print(f"Model {model} failed: {e}")
            continue

    return "Gemma did not respond."

def fetch_references(query):
    return [
        "https://en.wikipedia.org/wiki/" + "_".join(query.split()),
        "https://www.google.com/search?q=" + "+".join(query.split())
    ]

# ---------------- API Routes ---------------- #
@app.route('/api/text', methods=['POST'])
def api_text():
    user_input = request.json.get("text_input", "").strip()
    
    # Handle language switching
    if any(word in user_input.lower() for word in ["bhasha badlo", "change language"]):
        response_text = switch_language(user_input)
        references = []
        image_url = None
    else:
        response_text = query_gemma(user_input)
        references = fetch_references(user_input)
        image_url = None
        if "show me" in user_input.lower() or "image" in user_input.lower():
            image_path = generate_image(user_input)
            if image_path:
                image_url = f"/static/{os.path.basename(image_path)}"

    return jsonify({
        "response": response_text,
        "references": references,
        "image_url": image_url
    })

# ---------------- Run App ---------------- #
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
