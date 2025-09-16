import os
import requests
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv(".env.local")
load_dotenv(".env")

logger = logging.getLogger("tools")


# -----------------------------
# 🔍 Web Search Tool (SerpAPI)
# -----------------------------
def search_web(query: str) -> str:
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "❌ Missing SERPAPI_API_KEY in environment."

    url = "https://serpapi.com/search"
    params = {"q": query, "api_key": api_key}

    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()

        if "organic_results" in data and len(data["organic_results"]) > 0:
            first_result = data["organic_results"][0]
            title = first_result.get("title", "No title")
            snippet = first_result.get("snippet", "No snippet")
            link = first_result.get("link", "")
            return f"Top search result: {title}\n{snippet}\n{link}"
        return "No results found."
    except Exception as e:
        logger.error(f"Search error: {e}")
        return f"Search failed: {str(e)}"


# -----------------------------
# ☀️ Weather Tool (OpenWeatherMap)
# -----------------------------
def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "❌ Missing OPENWEATHER_API_KEY in environment."

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()

        if data.get("cod") != 200:
            return f"Weather API error: {data.get('message', 'Unknown error')}"

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]

        return f"The weather in {city} is {weather}, {temp}°C (feels like {feels}°C)."
    except Exception as e:
        logger.error(f"Weather error: {e}")
        return f"Weather lookup failed: {str(e)}"


# -----------------------------
# 📧 Email Tool (Gmail SMTP)
# -----------------------------
def send_email(recipient: str, subject: str, body: str) -> str:
    try:
        gmail_user = os.getenv("GMAIL_USER")
        gmail_pass = os.getenv("GMAIL_APP_PASSWORD")

        if not gmail_user or not gmail_pass:
            return "❌ Gmail credentials are not set. Configure GMAIL_USER and GMAIL_PASS in .env."

        msg = MIMEMultipart()
        msg["From"] = gmail_user
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(gmail_user, gmail_pass)
            server.sendmail(gmail_user, recipient, msg.as_string())

        return f"✅ Email successfully sent to {recipient}."
    except Exception as e:
        logger.error(f"Email error: {e}")
        return f"❌ Failed to send email: {str(e)}"