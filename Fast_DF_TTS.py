import asyncio
import edge_tts
import tempfile
import threading
import os
from playsound import playsound

VOICE = 'en-IE-ConnorNeural'
RATE = '+20%'

async def create_audio(text: str, output_file: str) -> None:
    communicator = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicator.save(output_file)

def play_audio(output_file: str) -> None:
    try:
        playsound(output_file)
    finally:
        try:
            os.remove(output_file)
        except OSError:
            pass

def speak(text: str) -> None:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            output_file = tmpfile.name

        asyncio.run(create_audio(text, output_file))
        threading.Thread(target=play_audio, args=(output_file,), daemon=True).start()

    except Exception as e:
        print(e)

def main() -> None:
    while True:
        try:
            text = input()
        except EOFError:
            break
        speak(text)


if __name__ == "__main__":
    main()
