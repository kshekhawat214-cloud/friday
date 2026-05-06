# 🤖 Friday — AI Voice Assistant

> *"Good morning, sir. I am Friday, your personal AI assistant."*

Friday is a local, offline-first AI voice assistant built in Python — inspired by Iron Man's J.A.R.V.I.S. It listens for a custom wake word, understands natural language commands, and controls your PC hands-free.

---

## ✨ Features

- 🎙️ **Wake Word Detection** — Activates on a custom "Friday" wake word using Picovoice Porcupine
- 🗣️ **Speech-to-Text** — Transcribes your voice commands locally using `faster-whisper`
- 🔊 **Text-to-Speech** — Responds with a natural voice via `pyttsx3`
- 🧠 **Intent Parsing & Routing** — Understands and routes commands to the right tool
- 📋 **Multi-Command Support** — Can handle chained commands in a single sentence
- 🧩 **Context Memory** — Remembers the last command and app for follow-up actions
- 💻 **App Launcher** — Opens installed apps by name, with smart registry lookup
- 🌐 **Web Search & Browser Control** — Searches the web or opens websites on command
- 📊 **System Monitor** — Tracks system stats in the background
- 📝 **Command Logger** — Logs all voice commands for history and debugging
- 🔄 **Alias Learning** — Learns your custom names for apps and commands

---

## 🗂️ Project Structure

```
friday_v1/
├── main.py                  # Entry point — starts Friday
├── requirements.txt         # Python dependencies
│
├── brain/                   # Core AI logic
│   ├── friday_brain.py      # Main command processor
│   ├── intent_parser.py     # Parses intent from natural language
│   ├── command_router.py    # Routes intents to the right tool
│   ├── command_normalizer.py# Fixes speech-to-text mistakes
│   ├── command_splitter.py  # Splits chained commands
│   ├── task_queue.py        # Queues and runs tasks
│   ├── alias_learner.py     # Learns custom app/command aliases
│   ├── smart_matcher.py     # Fuzzy matching for commands
│   └── logger.py            # Command history logger
│
├── interface/               # Input/Output layer
│   ├── wake_word.py         # Porcupine wake word listener
│   ├── speech_to_text.py    # Whisper-based voice transcription
│   └── text_to_speech.py    # pyttsx3 voice output
│
├── tools/                   # Action modules
│   ├── tool_manager.py      # Loads and manages tools
│   ├── app_registry.py      # Builds registry of installed apps
│   ├── open_app.py          # Launches desktop applications
│   ├── open_website.py      # Opens URLs in browser
│   ├── open_first_result.py # Opens first web search result
│   ├── search.py            # Web search tool
│   └── system_control.py   # System-level controls
│
├── memory/                  # Context & memory
├── models/                  # Porcupine wake word model (.ppn)
├── data/                    # App registry & persistent data
└── logs/                    # Command logs
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A microphone
- A [Picovoice account](https://console.picovoice.ai/) for the Porcupine access key

### 1. Clone the repo

```bash
git clone https://github.com/kshekhawat214-cloud/friday.git
cd friday
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r friday_v1/requirements.txt
pip install pvporcupine pyaudio
```

### 4. Configure your Porcupine Access Key

Open `friday_v1/interface/wake_word.py` and replace the `ACCESS_KEY` with your own key from [Picovoice Console](https://console.picovoice.ai/):

```python
ACCESS_KEY = "your-access-key-here"
```

### 5. Run Friday

```bash
cd friday_v1
python main.py
```

Friday will say **"Friday online"** and start listening for the wake word.

---

## 🎤 Example Commands

| You say | Friday does |
|---|---|
| *"Friday"* | Activates and listens |
| *"Open Chrome"* | Launches Google Chrome |
| *"Search Python tutorials"* | Searches the web |
| *"Open YouTube"* | Opens youtube.com |
| *"What's my CPU usage?"* | Reports system stats |

---

## 🛠️ Tech Stack

| Component | Library |
|---|---|
| Wake Word | [Picovoice Porcupine](https://picovoice.ai/platform/porcupine/) |
| Speech-to-Text | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) |
| Text-to-Speech | [pyttsx3](https://pyttsx3.readthedocs.io/) |
| Audio I/O | [sounddevice](https://python-sounddevice.readthedocs.io/), [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) |
| Numerics | [numpy](https://numpy.org/) |

---

## 📄 License

This project is private and not licensed for public use.

---

*Built with 🔥 by [kshekhawat214-cloud](https://github.com/kshekhawat214-cloud)*
