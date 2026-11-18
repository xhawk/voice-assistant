import pytest
import numpy as np
from unittest.mock import patch, MagicMock
from voice_assistant.audio import Recorder


class TestRecorder:
    @patch("voice_assistant.audio.recorder.sd.rec")
    @patch("voice_assistant.audio.recorder.sd.wait")
    def test_record_returns_bytes(self, mock_wait, mock_rec):
        mock_audio = np.zeros(48000, dtype=np.int16)
        mock_rec.return_value = mock_audio

        recorder = Recorder(duration=3.0, sample_rate=16000)
        result = recorder.record()

        assert isinstance(result, bytes)
        mock_rec.assert_called_once_with(48000, samplerate=16000, channels=1, dtype=np.int16)

    @patch("voice_assistant.audio.recorder.sd.rec")
    @patch("voice_assistant.audio.recorder.sd.wait")
    def test_record_custom_duration(self, mock_wait, mock_rec):
        mock_audio = np.zeros(8000, dtype=np.int16)
        mock_rec.return_value = mock_audio

        recorder = Recorder(duration=0.5, sample_rate=16000)
        recorder.record()

        mock_rec.assert_called_once_with(8000, samplerate=16000, channels=1, dtype=np.int16)

    @patch("voice_assistant.audio.recorder.sd.rec")
    @patch("voice_assistant.audio.recorder.sd.wait")
    def test_record_custom_sample_rate(self, mock_wait, mock_rec):
        mock_audio = np.zeros(44100, dtype=np.int16)
        mock_rec.return_value = mock_audio

        recorder = Recorder(duration=3.0, sample_rate=44100)
        recorder.record()

        mock_rec.assert_called_once_with(132300, samplerate=44100, channels=1, dtype=np.int16)
