Youtube link pasted here :- to view the working 

https://youtu.be/v17l8DHUgYk

Shiksha Mitra is a lightweight, multimodal learning assistant that helps students get quality educational support, even in areas with poor internet or in rural locations. The system works well on local hardware using Gemma models through Ollama. It also supports cloud-based processing when a connection is available.

Key Features

Multimodal Learning Support

- Generates diagrams, visuals, and organized notes
- Produces tables, summaries, and detailed solutions
- Offers quiz mode, practice mode, and scoring

Image Understanding

- Reads text from notebook photos
- Recognizes shapes, diagrams, and objects
- Solves handwritten math problems
- Provides clear visual explanations

Offline AI Processing (Gemma / Ollama)

- Operates fully offline with Gemma 2B/7B models
- Made for laptops and low-cost devices
- No internet needed for core functions

Personalized Learning

- Remembers session context for better flow
- Stores questions and answers in MongoDB
- Tracks progress and adjusts learning

Multilingual Support

- Supports English, Hindi, and can adapt to more languages
- Suitable for various learning situations

Architecture Overview

- Frontend: React
- Backend: Flask
- AI Models: Gemma (via Ollama), optional cloud models
- Database: MongoDB for logs and user progress
- Deployment: Offline-first with optional cloud backup

How It Works

The student asks a question, either in text or image form. The backend processes it using local AI models (Gemma). The response includes clear explanations, steps, or visuals. MongoDB keeps track of the prompt, response, and learning data. The frontend shows interactive results: explanations, quizzes, tables, and more.

Demo Video

(Insert your demo video link here)

[https://youtu.be/your_video_link](https://youtu.be/v17l8DHUgYk)

Project Structure
project/
│
├── frontend/          # React UI
├── backend/           # Flask API + Ollama/Gemma integration
├── database/          # MongoDB models and connectors
└── README.md

Current Capabilities

- Offline reasoning and explanation generation
- Diagram and visual creation through integration
- Image-based question solving
- Multilingual output
- Context-aware responses
- Learning mode and quiz mode

Setup Instructions
1. Install Frontend
cd frontend
npm install
npm run dev

2. Install Backend
cd backend
pip install -r requirements.txt
python app.py

3. Start Ollama (for Gemma models)
ollama pull gemma:2b
ollama run gemma:2b

4. Configure Environment

Create a .env file with:

MONGODB_URI=your_mongo_connect
OPENAI_API_KEY=optional

Why This Matters

Shiksha Mitra offers a meaningful solution for rural education by enabling AI-driven learning without the need for internet access. The goal is to close the digital gap for millions of students with limited resources.

Contributions

Contributions, ideas, and suggestions are welcome. Please open an issue or submit a pull request.


# Shiksha Mitra – Offline AI Tutor

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)

---

## 🚀 About the Project

Shiksha Mitra is a multilingual, multimodal offline AI tutor designed for students in low-connectivity areas.  
It can answer questions, generate diagrams, solve math problems from photos, and provide interactive learning tools — all without internet access.

Key highlights:

- **Multimodal Outputs:** Text, tables, diagrams, structured answers
- **Interactive Learning:** Quiz mode, practice mode, hints, scoring
- **Image Understanding:** OCR, object/shape recognition, math from notebook photos
- **Offline AI Processing:** Works on laptops or local servers with Gemma 2B / 7B
- **Persistent Memory:** Stores prompts and responses in MongoDB
- **Multilingual Support:** English, Hindi, Marathi, Gujarati, Russian, Bihari/Bhojpuri

---

## 🏗 Features

| Feature | Description |
|---------|-------------|
| **Text Q&A** | Ask questions and get detailed explanations with inline references |
| **Image Generation** | Generate diagrams or visuals using OpenAI |
| **Quiz / Practice Mode** | Interactive learning with hints and scoring |
| **Memory** | Keeps track of previous prompts and responses in MongoDB |
| **Offline Mode** | Run AI models locally without internet |
| **Multilingual** | Switch between multiple languages seamlessly |

---

## 🛠 Tech Stack

- **Frontend:** React.js
- **Backend:** Flask
- **AI Models:** Gemma 2B / 7B, OpenAI API (optional)
- **Database:** MongoDB
- **Deployment:** Render (backend), Vercel (frontend)
- **Other Tools:** Python-dotenv, Flask-CORS, OpenAI API

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Tutor_agent.git
cd Tutor_agent/backend


Contact

For collaboration or questions: sv695177@gmail.com
