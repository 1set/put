# -*- coding: UTF-8 -*-

from put.strutils import (
    str_after_first,
    str_after_last,
    str_before_first,
    str_before_last,
)

str_test_cases = [{
    "source": "hello.py",
    "substr": ".",
    "after_first": "py",
    "after_last": "py",
    "before_first": "hello",
    "before_last": "hello",
}, {
    "source": "hello.py",
    "substr": "~",
    "after_first": "",
    "after_last": "",
    "before_first": "",
    "before_last": "",
}, {
    "source": "hello.py",
    "substr": "",
    "after_first": "hello.py",
    "after_last": "",
    "before_first": "",
    "before_last": "hello.py",
}, {
    "source": "abc.def.ghi",
    "substr": ".",
    "after_first": "def.ghi",
    "after_last": "ghi",
    "before_first": "abc",
    "before_last": "abc.def",
}, {
    "source": "abc.def.ghi",
    "substr": "^",
    "after_first": "",
    "after_last": "",
    "before_first": "",
    "before_last": "",
}, {
    "source": "abc.def.ghi",
    "substr": "def",
    "after_first": ".ghi",
    "after_last": ".ghi",
    "before_first": "abc.",
    "before_last": "abc.",
}, {
    "source": "123123123",
    "substr": "124",
    "after_first": "",
    "after_last": "",
    "before_first": "",
    "before_last": "",
}, {
    "source": "123123123",
    "substr": "1",
    "after_first": "23123123",
    "after_last": "23",
    "before_first": "",
    "before_last": "123123",
}, {
    "source": "123123123",
    "substr": "124",
    "after_first": "",
    "after_last": "",
    "before_first": "",
    "before_last": "",
}, {
    "source": "123123123",
    "substr": "123",
    "after_first": "123123",
    "after_last": "",
    "before_first": "",
    "before_last": "123123",
}, {
    "source": "1111111111",
    "substr": "1",
    "after_first": "111111111",
    "after_last": "",
    "before_first": "",
    "before_last": "111111111",
}, {
    "source": "1111111111",
    "substr": "111",
    "after_first": "1111111",
    "after_last": "",
    "before_first": "",
    "before_last": "1111111",
}, {
    "source": "1111111111",
    "substr": "1111111111",
    "after_first": "",
    "after_last": "",
    "before_first": "",
    "before_last": "",
}, {
    "source": "1111111111",
    "substr": "11111111111",
    "after_first": "",
    "after_last": "",
    "before_first": "",
    "before_last": "",
}, {
    "source": "A",
    "substr": "A",
    "after_first": "",
    "after_last": "",
    "before_first": "",
    "before_last": "",
}, {
    "source": "",
    "substr": "",
    "after_first": "",
    "after_last": "",
    "before_first": "",
    "before_last": "",
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
