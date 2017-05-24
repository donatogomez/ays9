from enum import Enum


class EnumSchedulerStatus(Enum):
    halted = "halted"
    running = "running"
    stopping = "stopping"
