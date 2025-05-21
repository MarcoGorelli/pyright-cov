from __future__ import annotations

from typing import Generic, TypeVar

from numpy._typing._scalars import _UIntLike_co

def foo(a: _UIntLike_co) -> None:
    return None

def bar(a) -> None:
    return None

def bat(a: int) -> None:
    return None

__all__ = ['foo', 'bar', 'bat']

