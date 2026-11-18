import os
import pvporcupine
import sounddevice as sd
import numpy as np
from pathlib import Path


class WakeWord:
    def __init__(self, access_key: str | None = None):
        if access_key is None:
            access_key = os.getenv("PV_API_KEY")
        # Model path relative to project root
        keyword_path = str(
            Path(__file__).parent.parent.parent.parent.parent / "models" / "porcupine" / "Hei-koti_en_mac_v4_0_0.ppn"
        )
        self.porcupine = pvporcupine.create(keyword_paths=[keyword_path], access_key=access_key)

    def listen(self):
        print("Listening for wake word...")
        with sd.InputStream(
            samplerate=self.porcupine.sample_rate,
            channels=1,
            dtype=np.int16,
            blocksize=self.porcupine.frame_length,
        ) as stream:
            while True:
                audio = stream.read(self.porcupine.frame_length)[0]
                audio = audio.flatten().astype(np.int16)
                result = self.porcupine.process(audio)
                if result >= 0:
                    print("Wake word detected!")
                    return
