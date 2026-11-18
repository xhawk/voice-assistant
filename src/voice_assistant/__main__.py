import logging
from voice_assistant.config import load_config
from voice_assistant.ha import HAClient, CommandHandler, CommandResult
from voice_assistant.audio import WakeWord, Recorder
from voice_assistant.speech import STT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    config = load_config()
    ha_client = HAClient(base_url=config.ha_url, token=config.ha_token)
    handler = CommandHandler()
    stt = STT()
    recorder = Recorder(duration=3.0)
    wakeword = WakeWord(access_key=config.pv_api_key)

    def good_morning():
        response = ha_client.turn_on_scene("scene.hyvaa_huomenta")
        if response.status_code == 200:
            return CommandResult(success=True, message="Hyvää huomenta!")
        return CommandResult(success=False, message="Virhe")

    handler.register("Hyvää huomenta", good_morning)

    while True:
        wakeword.listen()
        audio = recorder.record()
        text = stt.transcribe(audio)
        logger.info(f"Transcribed: {text}")
        result = handler.handle(text)
        print(result.message)


if __name__ == "__main__":
    main()
