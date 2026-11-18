import httpx
import pytest
from unittest.mock import patch, Mock

from voice_assistant.ha import HAClient


@pytest.fixture
def ha_client():
    return HAClient(base_url="http://localhost:8123", token="test_token")


class TestHAClient:
    def test_headers(self, ha_client):
        headers = ha_client._headers()
        assert headers["Authorization"] == "Bearer test_token"
        assert headers["Content-Type"] == "application/json"

    @patch("voice_assistant.ha.client.httpx.Client")
    def test_turn_on_scene_success(self, mock_client_class, ha_client):
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 200

        mock_client = Mock()
        mock_client.post.return_value = mock_response
        mock_client_class.return_value.__enter__ = Mock(return_value=mock_client)
        mock_client_class.return_value.__exit__ = Mock(return_value=False)

        response = ha_client.turn_on_scene("scene.good_morning")

        mock_client.post.assert_called_once_with(
            "http://localhost:8123/api/services/scene/turn_on",
            json={"entity_id": "scene.good_morning"},
            headers=ha_client._headers(),
        )
        assert response.status_code == 200

    @patch("voice_assistant.ha.client.httpx.Client")
    def test_turn_on_scene_with_base_url_trailing_slash(self, mock_client_class, ha_client):
        ha_client_with_slash = HAClient(base_url="http://localhost:8123/", token="test_token")

        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 200

        mock_client = Mock()
        mock_client.post.return_value = mock_response
        mock_client_class.return_value.__enter__ = Mock(return_value=mock_client)
        mock_client_class.return_value.__exit__ = Mock(return_value=False)

        ha_client_with_slash.turn_on_scene("scene.good_night")

        mock_client.post.assert_called_once_with(
            "http://localhost:8123/api/services/scene/turn_on",
            json={"entity_id": "scene.good_night"},
            headers=ha_client_with_slash._headers(),
        )
