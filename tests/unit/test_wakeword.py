import pytest
from unittest.mock import patch, MagicMock, Mock
import numpy as np
from voice_assistant.audio import WakeWord


class TestWakeWord:
    @patch("voice_assistant.audio.wakeword.pvporcupine")
    def test_init_with_access_key(self, mock_porcupine):
        mock_instance = MagicMock()
        mock_porcupine.create.return_value = mock_instance

        WakeWord(access_key="test_key")

        mock_porcupine.create.assert_called_once()
        call_kwargs = mock_porcupine.create.call_args[1]
        assert call_kwargs["access_key"] == "test_key"
        assert "Hei-koti_en_mac_v4_0_0.ppn" in call_kwargs["keyword_paths"][0]

    @patch("voice_assistant.audio.wakeword.pvporcupine")
    def test_init_default_no_key(self, mock_porcupine):
        mock_instance = MagicMock()
        mock_porcupine.create.return_value = mock_instance

        WakeWord()

        mock_porcupine.create.assert_called_once()

    @patch("voice_assistant.audio.wakeword.sd.InputStream")
    @patch("voice_assistant.audio.wakeword.pvporcupine")
    def test_listen_returns_on_wake_word(self, mock_porcupine, mock_stream):
        mock_instance = MagicMock()
        mock_instance.sample_rate = 16000
        mock_instance.frame_length = 512
        mock_porcupine.create.return_value = mock_instance

        mock_audio = np.zeros(512, dtype=np.int16)
        mock_stream_instance = MagicMock()
        mock_stream_instance.read.return_value = (mock_audio, True)
        mock_stream.return_value.__enter__ = MagicMock(return_value=mock_stream_instance)
        mock_stream.return_value.__exit__ = Mock(return_value=False)

        mock_instance.process.return_value = 0

        wakeword = WakeWord()
        wakeword.listen()

        mock_stream_instance.read.assert_called()
