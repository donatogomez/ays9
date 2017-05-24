from enum import Enum


class EnumActionState(Enum):
    new = "new"
    changed = "changed"
    ok = "ok"
    scheduled = "scheduled"
    disabled = "disabled"
    error = "error"
    running = "running"
