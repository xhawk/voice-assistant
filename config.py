import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv


@dataclass
class Config:
    ha_url: str
    ha_token: str
    pv_api_key: str | None = None


def load_config(env_path: Path | None = None) -> Config:
    if env_path is None:
        env_path = Path(__file__).parent / ".env"
    load_dotenv(env_path)

    ha_url = os.getenv("HA_URL")
    ha_token = os.getenv("HA_TOKEN")
    pv_api_key = os.getenv("PV_API_KEY")

    missing = []
    if not ha_url:
        missing.append("HA_URL")
    if not ha_token:
        missing.append("HA_TOKEN")

    if missing:
        raise ValueError(f"Missing required config: {', '.join(missing)}")

    return Config(ha_url=ha_url, ha_token=ha_token, pv_api_key=pv_api_key)  # type: ignore[arg-type]
