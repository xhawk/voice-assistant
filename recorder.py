import logging
import numpy as np
import sounddevice as sd

from stt import STT

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


def main():
    logger.info("Recording...")
    recorder = Recorder(duration=3.0)
    audio_data = recorder.record()
    logger.info("Recording complete, transcribing...")

    stt = STT()
    text = stt.transcribe(audio_data)
    logger.info(f"Transcribed: {text}")


if __name__ == "__main__":
    main()
