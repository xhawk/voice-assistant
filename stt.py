import io
import numpy as np
from faster_whisper import WhisperModel


class STT:
    def __init__(self, model_size: str = "base", device: str = "auto"):
        self.model = WhisperModel(model_size, device=device, compute_type="int8")

    def transcribe(self, audio_data: bytes) -> str:
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        audio_float32 = audio_array.astype(np.float32) / 32768.0

        segments, info = self.model.transcribe(
            audio_float32,
            language="fi",
            beam_size=5,
        )

        text = " ".join(segment.text.strip() for segment in segments)
        return text
