import logging
import os
from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    RoomInputOptions,
    WorkerOptions,
    cli,
)
from livekit.agents.llm import function_tool
from livekit.plugins import google, deepgram, cartesia

# Import tools and persona system
from tools import search_web, get_weather, send_email
from personas import PersonaManager

logger = logging.getLogger("agent")

# Load environment variables
load_dotenv(".env.local")
load_dotenv(".env")

# Toggle debug mode to avoid real API calls
DEBUG_MODE = os.getenv("DEBUG_MODE", "1") == "1"

# -----------------------------
# 🤖 Assistant Agent Definition
# -----------------------------
class Assistant(Agent):
    def init(self):
        super().init(
            instructions="You are a helpful AI voice assistant. Keep responses clear and natural."
        )

    # Method to update instructions dynamically
    def update_instructions(self, instructions: str):
        self._instructions = instructions

    @function_tool
    async def search_web_tool(self, query: str):
        logger.info(f"🔍 Calling search_web with query: {query}")
        if DEBUG_MODE:
            return f"[DEBUG] Would search the web for: {query}"
        return search_web(query)

    @function_tool
    async def weather_tool(self, city: str):
        logger.info(f"☀️ Calling get_weather with city: {city}")
        if DEBUG_MODE:
            return f"[DEBUG] Would fetch weather for: {city}"
        return get_weather(city)

    @function_tool
    async def send_email(self, recipient: str, subject: str, body: str):
        logger.info(f"📧 Sending email to: {recipient}, subject: {subject}")
        if DEBUG_MODE:
            return f"[DEBUG] Would send email to {recipient} with subject '{subject}'"
        return send_email(recipient, subject, body)

    @function_tool
    async def switch_persona(self, persona: str):
        """Switch persona safely (instructions only)"""
        try:
            self.persona_manager.apply_persona(persona)
            return f"✅ Persona switched to {persona}."
        except ValueError:
            return f"❌ Unknown persona: {persona}. Try teacher, friend, or coach."


# -----------------------------
# 🔥 Prewarm Hook
# -----------------------------
def prewarm(proc: JobProcess):
    pass

# -----------------------------
# 🚀 Entrypoint
# -----------------------------
async def entrypoint(ctx: JobContext):
    ctx.log_context_fields = {"room": ctx.room.name}

    # Setup session with Gemini + STT + TTS (single female voice)
    session = AgentSession(
        llm=google.LLM(
            model="gemini-1.5-flash",
            api_key=os.getenv("GOOGLE_API_KEY"),
        ),
        stt=deepgram.STT(
            model="nova-3",
            language="en",
            api_key=os.getenv("DEEPGRAM_API_KEY"),
        ),
        tts=cartesia.TTS(
            voice="6f84f4b8-58a2-430c-8c79-688dad597532",  # original female voice
            api_key=os.getenv("CARTESIA_API_KEY"),
        ),
        preemptive_generation=True,
    )

    # Initialize assistant and persona manager
    assistant = Assistant()
    assistant.persona_manager = PersonaManager(session, assistant=assistant)

    # Start the session
    await session.start(
        agent=assistant,
        room=ctx.room,
        room_input_options=RoomInputOptions(),
    )

    # Greeting
    if DEBUG_MODE:
        logger.info("[DEBUG] BisonAI ready. Single female voice active.")
    else:
        session.say("Hi my name is BisonAI, your personal assistant. How can I make your day better?")

    await ctx.connect()

# -----------------------------
# 🏁 Main CLI Entrypoint
# -----------------------------
if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))