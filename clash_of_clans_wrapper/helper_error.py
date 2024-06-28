from typing import Any
from discord.ext import commands

class AttackerNotFound(commands.CommandError):
    def __init__(self, message: str | None = None, *args: Any) -> None:
        super().__init__(message, *args)

class ClientError(commands.CommandError):
    def __init__(self, reason = None,msg = None,type = None,detail = None, message: str | None = None, *args: Any) -> None:
        self.reason = reason
        self.msg = msg
        self.type = type
        self.detail = detail
        super().__init__(message, *args)

class InvalidAuth(ClientError):
    def __init__(self, reason=None, msg=None, type=None, detail=None, message: str | None = None, *args: Any) -> None:
        super().__init__(reason, msg, type, detail, message, *args)

class NotFound(ClientError):
    def __init__(self, reason=None, msg=None, type=None, detail=None, message: str | None = None, *args: Any) -> None:
        super().__init__(reason, msg, type, detail, message, *args)

class UnderMaintainance(ClientError):
    def __init__(self, reason=None, msg=None, type=None, detail=None, message: str | None = None, *args: Any) -> None:
        super().__init__(reason, msg, type, detail, message, *args)
