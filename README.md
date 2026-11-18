# Home Assistant Voice Client

Voice assistant client for Home Assistant with Finnish language support.

## Features

- **Wake word detection** using Picovoice Porcupine
- **Speech-to-text** using Faster Whisper (Finnish)
- **Command handling** for Home Assistant scenes

## Supported Platforms

- macOS
- Raspberry Pi 4 (Linux ARM64)

## Setup

```bash
cp .env.example .env
# Edit .env with your config
```

Required environment variables:
- `HA_URL` - Home Assistant URL (e.g., http://192.168.1.100:8123)
- `HA_TOKEN` - Long-lived access token
- `PV_API_KEY` - Picovoice API key (free at picovoice.ai)

### Raspberry Pi 4 Setup

```bash
# Install portaudio
sudo apt-get install portaudio19-dev

# Download Linux (ARM64) wake word model from Picovoice console
# Place it in models/porcupine/Hei-koti_en_mac_v4_0_0.ppn
```

## Run

```bash
uv run python -m voice_assistant
```

### Raspberry Pi Performance Tip

Use "tiny" model for faster STT inference:

```python
# In src/voice_assistant/speech/stt.py
stt = STT(model_size="tiny")
```

## Project Structure

```
voice_assistant/
├── src/voice_assistant/           # Main package
│   ├── config/                   # Configuration management
│   ├── ha/                       # Home Assistant integration
│   ├── audio/                    # Audio capture and detection
│   └── speech/                   # Speech processing
├── models/                        # ML models and binary assets (gitignored)
│   └── porcupine/                # Porcupine wake word model files
├── tests/                        # Test suite
│   ├── unit/                     # Unit tests
│   └── integration/              # Integration tests
```

## Test

```bash
uv run pytest
```

## TODO

- [ ] Docker containerization
