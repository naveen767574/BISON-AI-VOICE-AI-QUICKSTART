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
```bash
agent.py # Main assistant agent (LiveKit entrypoint)
tools.py # Tools: web search, weather lookup, email
personas.py # Persona definitions & manager
requirements.txt # Python dependencies
.env # Environment variables (API keys, secrets)

---

##⚙️ Installation
```bash
Clone the repo
git clone https://github.com/yourusername/bisonai.git
cd bisonai

