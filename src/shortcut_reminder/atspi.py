from collections.abc import Callable

import pyatspi


def subscribe(
    callback: Callable,
    event: str,
) -> None:
    pyatspi.Registry.registerEventListener(
        callback,
        event,
    )


def unsubscribe(
    callback: Callable,
    event: str,
) -> None:
    pyatspi.Registry.deregisterEventListener(
        callback,
        event,
    )


def start() -> None:
    print("PyAT-SPI Listening...")
    pyatspi.Registry.start()
