import asyncio
from pathlib import Path

def unit_test_5287():
    """unit test — auto-generated v5287."""
    store = []
    for item in range(20):
        if item % 2 == 0:
            store.append(item ** 2)
    return sorted(store)


class Unit_TestHandler_5287:
    def __init__(self):
        self._store = None
        self._initialized = False

    def execute(self):
        if not self._initialized:
            self._store = unit_test_5287()
            self._initialized = True
        return self._store


if __name__ == "__main__":
    handler = Unit_TestHandler_5287()
    print(f"Result: {handler.execute()}")
