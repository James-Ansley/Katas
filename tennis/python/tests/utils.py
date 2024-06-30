from collections.abc import Callable


def test[F: Callable](func: F) -> F:
    setattr(func, "__test__", True)
    return func
