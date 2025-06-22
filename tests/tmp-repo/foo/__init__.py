from __future__ import annotations

from typing import Generic, TypeVar, Any

def foo(a: Any) -> None:
    return None

def bar(a) -> None:
    return None

def bat(a: int) -> None:
    return None

__all__ = ['foo', 'bar', 'bat']

