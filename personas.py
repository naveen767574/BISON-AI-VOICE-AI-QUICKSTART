import logging

logger = logging.getLogger("personas")

# -----------------------------
# Define available personas
# -----------------------------
PERSONAS = {
    "teacher": {
        "instructions": "You are a kind, polite female teacher. Explain concepts clearly and step by step.",
        "voice": "6f84f4b8-58a2-430c-8c79-688dad597532",  # female voice
    },
    "friend": {
        "instructions": "You are a casual and funny best friend. Keep it light and friendly.",
        "voice": "a3c5b6d7-1234-5678-9abc-def012345678",  # change this ID
    },
    "coach": {
        "instructions": "You are a strict but motivating fitness coach. Push the user to do their best.",
        "voice": "b7e9d8f6-9876-5432-10fe-dcba98765432",  # change this ID
    },
}

# -----------------------------
# Persona accessor function
# -----------------------------
def get_persona(name: str) -> dict:
    """
    Return the persona configuration.
    Raises ValueError if persona is unknown.
    """
    if name not in PERSONAS:
        raise ValueError(f"Unknown persona: {name}")
    return PERSONAS[name]

# -----------------------------
# Persona manager class
# -----------------------------
class PersonaManager:
    """
    Optional helper to manage personas dynamically in a session.
    """
    def __init__(self, session, assistant=None, default: str = "teacher"):
        self.session = session
        self.assistant = assistant  # store the assistant object to update instructions
        self.current_persona = default
        self.apply_persona(default)

    def apply_persona(self, persona_name: str):
        if persona_name not in PERSONAS:
            logger.warning(f"Persona '{persona_name}' not found. Keeping current persona.")
            return

        persona_cfg = PERSONAS[persona_name]
        self.current_persona = persona_name

        # ✅ Use Agent.update_instructions from LiveKit
        if self.assistant:
            self.assistant.update_instructions(persona_cfg["instructions"])

        logger.info(f"🎭 Persona switched to '{persona_name}'.")
        logger.info(f"Instructions: {persona_cfg['instructions']}")
