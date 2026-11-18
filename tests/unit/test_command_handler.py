import pytest
from voice_assistant.ha import CommandHandler, CommandResult


class TestCommandHandler:
    def test_register_and_handle(self):
        handler = CommandHandler()

        def my_command():
            return CommandResult(success=True, message="Command executed")

        handler.register("hello", my_command)

        result = handler.handle("hello")

        assert result.success is True
        assert result.message == "Command executed"

    def test_handle_not_found(self):
        handler = CommandHandler()

        result = handler.handle("unknown command")

        assert result.success is False
        assert result.message == "En tiedä mitä tarkoitit"

    def test_handle_case_insensitive(self):
        handler = CommandHandler()

        def my_command():
            return CommandResult(success=True, message="OK")

        handler.register("hello", my_command)

        result = handler.handle("HELLO")

        assert result.success is True

    def test_multiple_commands(self):
        handler = CommandHandler()

        def cmd1():
            return CommandResult(success=True, message="one")

        def cmd2():
            return CommandResult(success=True, message="two")

        handler.register("one", cmd1)
        handler.register("two", cmd2)

        assert handler.handle("one").message == "one"
        assert handler.handle("two").message == "two"
