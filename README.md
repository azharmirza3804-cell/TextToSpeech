# 🔊 TextToSpeech

<div align="center">

### 🎙️ Python Text-to-Speech Collection

**Convert text into speech using multiple Python TTS approaches.**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/azharmirza3804-cell/TextToSpeech)
[![TTS](https://img.shields.io/badge/Project-Text--to--Speech-purple)](https://github.com/azharmirza3804-cell/TextToSpeech)

</div>

---

## 📖 About

**TextToSpeech** is a Python project that demonstrates different ways to convert text into spoken audio.

The repository contains multiple implementations so you can experiment with:

* 🖥️ Offline text-to-speech
* 🌐 Online neural text-to-speech
* 🎵 MP3 generation and playback
* 🎤 Voice selection
* ⚡ Fast/background audio playback
* 🤖 JARVIS-style voice assistants
* 🔌 Optional API-based speech generation

The project is especially useful if you are building a **Python voice assistant, AI assistant, chatbot, automation tool, or accessibility application**.

---

## ✨ Features

| Feature                |  Supported |
| ---------------------- | :--------: |
| Python TTS             |      ✅     |
| Offline TTS            |      ✅     |
| Microsoft Edge TTS     |      ✅     |
| Neural voices          |      ✅     |
| MP3 generation         |      ✅     |
| Audio playback         |      ✅     |
| Voice selection        |      ✅     |
| Adjustable speech rate |      ✅     |
| Adjustable volume      |      ✅     |
| Background playback    |      ✅     |
| StreamElements API     | ✅ Optional |
| JARVIS-style assistant |      ✅     |

---

# 🧰 Technologies

This project uses several Python libraries depending on the implementation:

* 🐍 **Python**
* 🔊 **pyttsx3**
* 🌐 **edge-tts**
* 🎵 **pygame**
* 🔉 **playsound**
* 🌍 **requests**
* 🌐 **Selenium**
* 🚗 **webdriver-manager**
* ⚡ **asyncio**
* 🧵 **threading**

---

# 📂 Project Structure

```text
TextToSpeech/
│
├── Fast_DF_TTS.py
├── TTS_DF.py
├── TextToSpeech_B.py
├── TextToSpeech_python.py
├── ttsB.py
│
└── README.md
```

---

# 📄 File Guide

## 🔹 `TextToSpeech_python.py`

The simplest implementation in the repository.

It uses **`pyttsx3`** to convert text into speech using voices available on the local system.

```python
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()
```

### Example

```python
from TextToSpeech_python import speak

speak("Hello, I am your personal assistant.")
```

### Best for

* Beginners
* Offline applications
* Simple voice output
* Python experiments

---

# 🔹 `TextToSpeech_B.py`

A more configurable **`pyttsx3`** implementation.

It:

* Sets speech rate
* Sets volume
* Searches installed voices
* Attempts to find a voice named **George**
* Provides JARVIS-style example messages

The current implementation uses a speech rate of `170` and volume `1.0`.

### Example

```python
speak("Hello")
speak("I am Jarvis, your personal assistant.")
speak("What can I help you?")
```

---

# 🔹 `Fast_DF_TTS.py`

A fast **Microsoft Edge TTS** implementation using:

```text
edge-tts
playsound
asyncio
threading
```

The current implementation uses:

```text
Voice: en-IE-ConnorNeural
Rate: +20%
```

It generates a temporary MP3 file and plays it in a background thread before cleaning up the temporary file.

### Run

```bash
python Fast_DF_TTS.py
```

Then type text into the terminal.

Example:

```text
Hello, I am your AI assistant.
```

---

# 🔹 `TTS_DF.py`

Another **Edge TTS** implementation, this time using **Pygame** for audio playback.

The current voice is:

```text
en-IE-ConnorNeural
```

The implementation generates `speech.mp3` by default and plays it using `pygame.mixer`.

### Example

```python
speak("Hello sir, how can I help you today?")
```

---

# 🔹 `ttsB.py`

This implementation provides two speech-generation modes.

### 🌐 Online Mode

When the environment variable

```text
STREAMELEMENTS_API_KEY
```

is available, the script requests speech audio from the StreamElements speech endpoint.

### 💻 Offline Fallback

When the API key is not configured, the script automatically uses **`pyttsx3`**.

The implementation can select an installed voice, configure speech rate/volume, generate/play an MP3 for the API path, and remove the temporary audio file afterward.

### Example

```python
speak("Hello sir, I am Jarvis")
```

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/azharmirza3804-cell/TextToSpeech.git
```

## 2. Open the project

```bash
cd TextToSpeech
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

Install the libraries required by the different implementations:

```bash
pip install pyttsx3
pip install edge-tts
pip install pygame
pip install playsound==1.2.2
pip install requests
pip install selenium
pip install webdriver-manager
```

Or install them together:

```bash
pip install pyttsx3 edge-tts pygame playsound==1.2.2 requests selenium webdriver-manager
```

> **Note:** You don't need every package if you only want to use one TTS implementation.

---

# ▶️ Quick Start

## Option 1 — Offline TTS

```bash
python TextToSpeech_python.py
```

Or use it from another Python program:

```python
from TextToSpeech_python import speak

speak("Hello! Welcome to my Text-to-Speech project.")
```

---

## Option 2 — Fast Edge TTS

```bash
python Fast_DF_TTS.py
```

Enter text:

```text
Hello! Welcome to my AI assistant.
```

The program generates speech and plays the resulting audio.

---

## Option 3 — Edge TTS + Pygame

```bash
python TTS_DF.py
```

The script demonstrates Edge TTS speech generation followed by Pygame playback.

---

## Option 4 — Automatic Online/Offline TTS

```bash
python ttsB.py
```

If `STREAMELEMENTS_API_KEY` is configured, the API-based path is used.

Otherwise, the program falls back to `pyttsx3`.

---

# 🎤 Basic `pyttsx3` Example

```python
import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

engine.say("Hello! I am your personal assistant.")
engine.runAndWait()
```

### Change speech speed

```python
engine.setProperty("rate", 200)
```

### Change volume

```python
engine.setProperty("volume", 0.8)
```

---

# 🌐 Basic Edge TTS Example

Install:

```bash
pip install edge-tts
```

Example:

```python
import asyncio
import edge_tts

async def generate_speech(text):
    voice = "en-IE-ConnorNeural"

    communicator = edge_tts.Communicate(
        text,
        voice
    )

    await communicator.save("speech.mp3")

asyncio.run(
    generate_speech(
        "Hello! This is Microsoft Edge Text-to-Speech."
    )
)
```

---

# 🔐 StreamElements API

The `ttsB.py` implementation can optionally use a StreamElements API key.

Set the key as an environment variable.

### Windows PowerShell

```powershell
$env:STREAMELEMENTS_API_KEY="YOUR_API_KEY"
```

### Windows CMD

```cmd
set STREAMELEMENTS_API_KEY=YOUR_API_KEY
```

### Linux / macOS

```bash
export STREAMELEMENTS_API_KEY="YOUR_API_KEY"
```

Then:

```bash
python ttsB.py
```

### ⚠️ Never expose your API key

Do **not** put secrets directly inside your Python source code.

❌ Don't do this:

```python
api_key = "MY_SECRET_API_KEY"
```

✅ Use an environment variable:

```python
import os

api_key = os.getenv("STREAMELEMENTS_API_KEY")
```

Also make sure your `.env`, secret files, or credentials are included in `.gitignore`.

---

# 🧠 How It Works

The general workflow is:

```text
          ┌─────────────────┐
          │   User Input    │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  TTS Function   │
          └────────┬────────┘
                   │
          ┌────────┴─────────┐
          │                  │
          ▼                  ▼
   ┌──────────────┐   ┌──────────────┐
   │   pyttsx3    │   │   Edge TTS   │
   │    Offline   │   │    Online    │
   └──────┬───────┘   └──────┬───────┘
          │                  │
          └────────┬─────────┘
                   ▼
          ┌─────────────────┐
          │ Audio Playback  │
          └─────────────────┘
```

---

# ⚖️ TTS Comparison

| Feature             |      pyttsx3      | Edge TTS |   StreamElements  |
| ------------------- | :---------------: | :------: | :---------------: |
| Internet            |         ❌         |     ✅    |         ✅         |
| Offline             |         ✅         |     ❌    |         ❌         |
| Neural voices       | Depends on system |     ✅    | Service dependent |
| MP3 output          |      Limited      |     ✅    |         ✅         |
| Voice selection     |         ✅         |     ✅    |         ✅         |
| API key             |         ❌         |     ❌    |      Optional     |
| Simple setup        |       ⭐⭐⭐⭐⭐       |   ⭐⭐⭐⭐   |        ⭐⭐⭐        |
| Good for assistants |         ✅         |     ✅    |         ✅         |

---

# 🤖 JARVIS Example

This repository can serve as the **voice/output component of a personal AI assistant**.

Example:

```python
from TextToSpeech_python import speak

speak("Hello sir.")
speak("I am Jarvis, your personal assistant.")
speak("How can I help you today?")
```

A complete assistant could eventually follow this architecture:

```text
              ┌───────────────┐
              │     USER      │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Voice / Text  │
              │     Input     │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │  AI / Logic   │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Text-to-Speech│
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │     VOICE     │
              └───────────────┘
```

---

# 💡 Possible Use Cases

This project can be used as a foundation for:

* 🤖 AI personal assistants
* 🎙️ Voice assistants
* 💬 Chatbots
* 🏠 Smart-home systems
* 🎮 Games and NPCs
* 📚 Educational software
* ♿ Accessibility applications
* 🔔 Notification systems
* 🧑‍💻 Automation tools
* 🗣️ Voice-based applications

---

# 🛠️ Troubleshooting

### 🔇 No sound with `pyttsx3`

Test your local speech engine:

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("Testing text to speech")
engine.runAndWait()
```

If necessary:

```bash
pip install --upgrade pyttsx3
```

---

### 🔊 Pygame audio problem

Try:

```bash
pip install --upgrade pygame
```

Also check that your operating system has a working audio output device.

---

### 🎵 `playsound` problem

This project uses:

```bash
pip install playsound==1.2.2
```

Using a different version may result in compatibility issues with some environments.

---

### 🌐 Edge TTS problem

Make sure your internet connection is working and update the package:

```bash
pip install --upgrade edge-tts
```

---

# 🔮 Future Improvements

Potential improvements for this project:

* [ ] 🎤 Speech-to-Text integration
* [ ] 🤖 AI chatbot integration
* [ ] 🧠 Full JARVIS assistant
* [ ] 🌍 Multi-language support
* [ ] 🎙️ More voice options
* [ ] 🎚️ Voice speed/pitch controls
* [ ] 🖥️ Graphical user interface
* [ ] 🌐 Web interface
* [ ] 📱 Application interface
* [ ] 💾 Audio file management
* [ ] 🧪 Automated tests
* [ ] 📦 `requirements.txt`
* [ ] 🔄 GitHub Actions
* [ ] 📚 API documentation

---

# 🤝 Contributing

Contributions are welcome!

### 1. Fork the repository

### 2. Create a branch

```bash
git checkout -b feature/my-feature
```

### 3. Make your changes

### 4. Commit

```bash
git add .
git commit -m "Add new TTS feature"
```

### 5. Push

```bash
git push origin feature/my-feature
```

### 6. Open a Pull Request

---

# 📜 License

A license file is not currently included in this repository.

If you plan to make this project open source, consider adding an appropriate license such as the **MIT License**.

---

# 👨‍💻 Author

## Azhar Mirza

GitHub:

**https://github.com/azharmirza3804-cell**

Project:

**https://github.com/azharmirza3804-cell/TextToSpeech**

---

# ⭐ Support the Project

If you find this project useful:

⭐ **Star** the repository
🍴 **Fork** the repository
🐛 **Report** bugs
💡 **Suggest** improvements
🤝 **Contribute** to the project

---

<div align="center">

### 🔊 Give Your Python Projects a Voice

**Built with 🐍 Python and ❤️ by Azhar Mirza**

</div>


