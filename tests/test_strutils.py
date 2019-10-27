# -*- coding: UTF-8 -*-

from put.strutils import (
    str_after_first,
    str_after_last,
    str_before_first,
    str_before_last,
)

string_test_cases = [
    ("hello.py", "."),
    ("hello.py", "-"),
    ("hello.py", ""),
    ("abc.def.ghi", "."),
    ("abc.def.ghi", "-"),
    ("abc.def.ghi", ""),
    ("123123123", "1"),
    ("123123123", "4"),
    ("123123123", "123"),
    ("123123123", ""),
    ("abcabcabc", "abc"),
    ("1abc2abc3abc4", "abc"),
    ("abc", "abc"),
    ("A", "A"),
    ("", ""),
]

str_test_cases = [{
    "source": "hello.py",
    "substr": ".",
    "after_first": "py",
    "after_last": "py",
    "before_first": "hello",
    "before_last": "hello",
}]


def test_str_after_first():
    for tc in str_test_cases:
        assert str_after_first(tc['source'], tc['substr']) == tc['after_first']


def test_str_after_last():
    for tc in str_test_cases:
        assert str_after_last(tc['source'], tc['substr']) == tc['after_last']


def test_str_before_first():
    for tc in str_test_cases:
        assert str_before_first(tc['source'], tc['substr']) == tc['before_first']


def test_str_before_last():
    for tc in str_test_cases:
        assert str_before_last(tc['source'], tc['substr']) == tc['before_last']
