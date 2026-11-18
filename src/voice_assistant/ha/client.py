import httpx


class HAClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def turn_on_scene(self, entity_id: str) -> httpx.Response:
        url = f"{self.base_url}/api/services/scene/turn_on"
        payload = {"entity_id": entity_id}
        with httpx.Client() as client:
            return client.post(url, json=payload, headers=self._headers())
