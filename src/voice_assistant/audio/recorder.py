import logging
import numpy as np
import sounddevice as sd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Recorder:
    def __init__(self, duration: float = 5.0, sample_rate: int = 16000):
        self.duration = duration
        self.sample_rate = sample_rate

    def record(self) -> bytes:
        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype=np.int16,
        )
        sd.wait()
        return audio.tobytes()
