# 🦬 BisonAI – AI Voice Assistant  

BisonAI is a real-time AI voice assistant built with [LiveKit](https://livekit.io/), [Google Gemini](https://ai.google/), [Deepgram](https://deepgram.com/), and [Cartesia](https://cartesia.ai/).  
It can **search the web**, **fetch weather updates**, **send emails**, and even **switch personas** (teacher, friend, coach) for more natural conversations.  

---

## ✨ Features
- 🎤 **Real-time voice interaction** using Deepgram STT + Cartesia TTS.  
- 🔍 **Web search** powered by SerpAPI.  
- ☀️ **Weather updates** with OpenWeatherMap API.  
- 📧 **Email sending** via Gmail SMTP.  
- 🎭 **Dynamic personas** – teacher, friend, or coach.  
- 🤖 Powered by **Google Gemini** for natural language reasoning.  

---

## 📂 Project Structure
├── agent.py # Main assistant agent (LiveKit entrypoint)
├── tools.py # Tools: web search, weather lookup, email
├── personas.py # Persona definitions & manager
├── requirements.txt # Python dependencies
└── .env # Environment variables (API keys, secrets)


---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/bisonai.git
   cd bisonai


Create a virtual environment

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

Install dependencies

pip install -r requirements.txt


🔑 Environment Setup

Create a .env file in the project root with your keys:
# Google Gemini
GOOGLE_API_KEY=your_google_key_here

# Deepgram
DEEPGRAM_API_KEY=your_deepgram_key_here

# Cartesia
CARTESIA_API_KEY=your_cartesia_key_here

# SerpAPI (for web search)
SERPAPI_API_KEY=your_serpapi_key_here

# OpenWeather
OPENWEATHER_API_KEY=your_openweather_key_here

# Gmail (for email sending)
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password


🚀 Usage

Run the assistant with:

python agent.py

The assistant will join your LiveKit room and greet you:

“Hi my name is BisonAI, your personal assistant. How can I make your day better?”

🎭 Personas

Switch between personas to change the assistant’s tone:

Teacher – polite, clear, step-by-step explanations.

Friend – casual, friendly, light-hearted.

Coach – strict, motivational, pushy.


📌 Roadmap

 Add more personas (doctor, storyteller, mentor).

 Add task management (to-do lists, reminders).

 Integrate with calendar APIs.

 Expand TTS voices.

🛡️ License

MIT License – feel free to use and modify.

🙌 Acknowledgments

LiveKit Agents SDK

Google Gemini

Deepgram

Cartesia

SerpAPI

OpenWeather
