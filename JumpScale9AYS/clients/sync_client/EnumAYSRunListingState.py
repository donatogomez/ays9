from enum import Enum


class EnumAYSRunListingState(Enum):
    new = "new"
    running = "running"
    ok = "ok"
    error = "error"
