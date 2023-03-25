import threading
from typing import Any


class ThreadSafeSingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]


class ThreadSafeSingleton(metaclass=ThreadSafeSingletonMeta):
    def some_logic(self):
        pass
