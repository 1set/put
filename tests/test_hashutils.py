import pytest
from put.hashutils import md5str


__author__ = "Angel Analoosen"
__copyright__ = "Angel Analoosen"
__license__ = "MIT License"


def test_md5str():
    assert md5str("") == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5str("A") == "7fc56270e7a70fa81a5935b72eacbe29"
    assert md5str("123456") == "e10adc3949ba59abbe56e057f20f883e"
