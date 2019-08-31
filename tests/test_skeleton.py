# -*- coding: utf-8 -*-

import pytest
from put.skeleton import fib

__author__ = "Angel Analoosen"
__copyright__ = "Angel Analoosen"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
