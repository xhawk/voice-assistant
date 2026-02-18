import logging
from dataclasses import dataclass
from typing import Callable

logger = logging.getLogger(__name__)


@dataclass
class CommandResult:
    success: bool
    message: str


class CommandHandler:
    def __init__(self):
        self.commands: dict[str, callable] = {}

    def register(self, text: str, handler: callable):
        self.commands[text.lower()] = handler

    def handle(self, text: str) -> CommandResult:
        key = text.lower()
        if key in self.commands:
            return self.commands[key]()

        logger.info("no match found")
        return CommandResult(success=False, message="En tiedä mitä tarkoitit")
