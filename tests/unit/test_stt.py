import pytest
import numpy as np
from unittest.mock import patch, MagicMock
from voice_assistant.speech import STT


class TestSTT:
    @patch("voice_assistant.speech.stt.WhisperModel")
    def test_transcribe_returns_text(self, mock_whisper_model):
        mock_model_instance = MagicMock()
        mock_segment = MagicMock()
        mock_segment.text = "Hyvää huomenta"
        mock_model_instance.transcribe.return_value = ([mock_segment], MagicMock())
        mock_whisper_model.return_value = mock_model_instance

        stt = STT()
        audio_data = (np.zeros(16000, dtype=np.int16)).tobytes()

        result = stt.transcribe(audio_data)

        assert result == "Hyvää huomenta"

    @patch("voice_assistant.speech.stt.WhisperModel")
    def test_transcribe_multiple_segments(self, mock_whisper_model):
        mock_model_instance = MagicMock()
        mock_segment1 = MagicMock()
        mock_segment1.text = "Hyvää"
        mock_segment2 = MagicMock()
        mock_segment2.text = "huomenta"
        mock_model_instance.transcribe.return_value = (
            [mock_segment1, mock_segment2],
            MagicMock(),
        )
        mock_whisper_model.return_value = mock_model_instance

        stt = STT()
        audio_data = (np.zeros(16000, dtype=np.int16)).tobytes()

        result = stt.transcribe(audio_data)

        assert result == "Hyvää huomenta"

    @patch("voice_assistant.speech.stt.WhisperModel")
    def test_transcribe_with_language_fi(self, mock_whisper_model):
        mock_model_instance = MagicMock()
        mock_segment = MagicMock()
        mock_segment.text = "test"
        mock_model_instance.transcribe.return_value = ([mock_segment], MagicMock())
        mock_whisper_model.return_value = mock_model_instance

        stt = STT()

        audio_data = (np.zeros(16000, dtype=np.int16)).tobytes()
        stt.transcribe(audio_data)

        call_kwargs = mock_model_instance.transcribe.call_args[1]
        assert call_kwargs["language"] == "fi"
