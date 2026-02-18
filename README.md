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
# Replace Hei-koti_en_mac_v4_0_0.ppn with Linux version
```

## Run

```bash
uv run python main.py
```

### Raspberry Pi Performance Tip

Use "tiny" model for faster STT inference:

```python
# In main.py or stt.py
stt = STT(model_size="tiny")
```

## Project Structure

- `main.py` - Main entry point
- `config.py` - Configuration loader
- `ha_client.py` - Home Assistant API client
- `wakeword.py` - Wake word detection
- `recorder.py` - Audio recorder
- `stt.py` - Speech-to-text
- `command_handler.py` - Command routing

## Test

```bash
uv run pytest
```

## TODO

- [ ] Docker containerization

