import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
from config import load_config, Config


class TestConfig:
    @patch("config.load_dotenv")
    @patch("config.Path.__truediv__")
    def test_load_config_success(self, mock_truediv, mock_load_dotenv):
        mock_env_path = Path(".env")
        mock_truediv.return_value = mock_env_path

        with patch("config.os.getenv") as mock_getenv:
            mock_getenv.side_effect = lambda key: {
                "HA_URL": "http://localhost:8123",
                "HA_TOKEN": "test_token",
            }.get(key)

            config = load_config()

        assert config == Config(ha_url="http://localhost:8123", ha_token="test_token")

    @patch("config.load_dotenv")
    @patch("config.Path.__truediv__")
    def test_load_config_missing_ha_url(self, mock_truediv, mock_load_dotenv):
        mock_env_path = Path(".env")
        mock_truediv.return_value = mock_env_path

        with patch("config.os.getenv") as mock_getenv:
            mock_getenv.side_effect = lambda key: {
                "HA_URL": None,
                "HA_TOKEN": "test_token",
            }.get(key)

            with pytest.raises(ValueError, match="Missing required config: HA_URL"):
                load_config()

    @patch("config.load_dotenv")
    @patch("config.Path.__truediv__")
    def test_load_config_missing_ha_token(self, mock_truediv, mock_load_dotenv):
        mock_env_path = Path(".env")
        mock_truediv.return_value = mock_env_path

        with patch("config.os.getenv") as mock_getenv:
            mock_getenv.side_effect = lambda key: {
                "HA_URL": "http://localhost:8123",
                "HA_TOKEN": None,
            }.get(key)

            with pytest.raises(ValueError, match="Missing required config: HA_TOKEN"):
                load_config()
