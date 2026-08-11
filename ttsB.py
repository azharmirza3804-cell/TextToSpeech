import requests # pip install requests
from playsound import playsound # pip install playsound==1.2.2
import pyttsx3
import os
from typing import Union # pip install typing

speech_engine = None

def generate_audio(message: str, voice: str = "Brian"):
    url: str = "https://api.streamelements.com/kappa/v2/speech"

    headers = {"User-Agent": "Mozilla/5.0"}
    api_key = os.getenv("STREAMELEMENTS_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    result = requests.get(
        url=url,
        params={"voice": voice, "text": message},
        headers=headers,
        timeout=30,
    )
    result.raise_for_status()
    if not result.headers.get("content-type", "").startswith("audio/"):
        raise RuntimeError("The speech service did not return an audio file.")
    return result.content

def speak(message: str, voice: str = "Brian", folder: str = "", extension: str = "mp3")->Union[None, str]:
    global speech_engine
    if not os.getenv("STREAMELEMENTS_API_KEY"):
        if speech_engine is None:
            speech_engine = pyttsx3.init()
            voices = speech_engine.getProperty("voices")
            selected_voice = next(
                (installed_voice for installed_voice in voices if voice.lower() in installed_voice.name.lower()),
                next((installed_voice for installed_voice in voices if "george" in installed_voice.name.lower()), None),
            )
            if selected_voice:
                speech_engine.setProperty("voice", selected_voice.id)
            speech_engine.setProperty("volume", 1.0)
            speech_engine.setProperty("rate", 220)
        speech_engine.say(message)
        speech_engine.runAndWait()
        return None

    file_path = os.path.join(folder, f"{voice}.{extension}")
    try:
        result_content = generate_audio(message, voice)
        with open(file_path, "wb") as file:
            file.write(result_content)
        playsound.playsound(file_path)
        return None
    except Exception as e:
        print(e)
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    speak("hello sir , i am jarvis")