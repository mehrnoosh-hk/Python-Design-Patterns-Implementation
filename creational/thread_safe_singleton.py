import threading
from typing import Any


class ThreadSafeSingletonMeta(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        with threading.Lock():
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]


class ThreadSafeSingleton(metaclass=ThreadSafeSingletonMeta):
    def some_logic():
        pass
