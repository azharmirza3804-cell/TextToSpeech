import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

logging.getLogger('selenium').setLevel(logging.WARNING)

chrome_option = Options()
chrome_option.add_argument("--headless")
chrome_option.add_argument("--log-level=3")
chrome_option.add_argument("--disable-blink-features=AutomationControlled")

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")
    george_voice = next(
        (
            voice
            for voice in voices
            if "george" in f"{voice.id} {getattr(voice, 'name', '')}".lower()
        ),
        None,
    )
    if george_voice:
        engine.setProperty("voice", george_voice.id)

    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak("hello")
speak("I am Jarvis, your personal assistant.")
speak("what can I help you?")
