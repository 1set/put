# -*- coding: UTF-8 -*-

import pytest
from put.hashutils import (md5str, md5sum, md5base64, sha1str, sha1sum, sha1base64, sha256str, sha256sum, sha256base64)


def test_md5str():
    assert md5str("") == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5str("A") == "7fc56270e7a70fa81a5935b72eacbe29"
    assert md5str("123456") == "e10adc3949ba59abbe56e057f20f883e"
    assert md5str("哦😯") == "4a552abe9132e1679d38f2ff876e63ba"
    with pytest.raises(TypeError):
        assert md5str(123)


def test_md5sum():
    assert md5sum("tests/resources/sample.zip") == "754c62de0f179e7f63aefe243273b29b"
    with pytest.raises(FileNotFoundError):
        assert md5sum("__read_a_file_not_exists__")


def test_md5base64():
    assert md5base64("tests/resources/sample.zip") == "dUxi3g8Xnn9jrv4kMnOymw=="
    with pytest.raises(FileNotFoundError):
        assert md5sum("__read_a_file_not_exists__")


def test_sha1str():
    assert sha1str("") == "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    assert sha1str("A") == "6dcd4ce23d88e2ee9568ba546c007c63d9131c1b"
    assert sha1str("123456") == "7c4a8d09ca3762af61e59520943dc26494f8941b"
    assert sha1str("哦😯") == "1c4285cf2396162ebf24e14f485d69dd45321e20"
    with pytest.raises(TypeError):
        assert sha1str(123)


def test_sha1sum():
    assert sha1sum("tests/resources/sample.zip") == "5f5878e1d9950e9a56583cd99534f6a48c1110c8"
    with pytest.raises(FileNotFoundError):
        assert sha1sum("__read_a_file_not_exists__")


def test_sha1base64():
    assert sha1base64("tests/resources/sample.zip") == "X1h44dmVDppWWDzZlTT2pIwREMg="
    with pytest.raises(FileNotFoundError):
        assert sha1sum("__read_a_file_not_exists__")


def test_sha256str():
    assert sha256str("") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert sha256str("A") == "559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd"
    assert sha256str("123456") == "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
    assert sha256str("哦😯") == "0344706917c9fce1954dc592c57618d7972666654e67961ab0b7f441ea4e8d9f"
    with pytest.raises(TypeError):
        assert sha256str(123)


def test_sha256sum():
    assert sha256sum("tests/resources/sample.zip") == "71a41b22c722bfa67774dcc86c94bb431546829a1bd1026692ea790c0a49de33"
    with pytest.raises(FileNotFoundError):
        assert sha256sum("__read_a_file_not_exists__")


def test_sha256base64():
    assert sha256base64("tests/resources/sample.zip") == "caQbIsciv6Z3dNzIbJS7QxVGgpob0QJmkup5DApJ3jM="
    with pytest.raises(FileNotFoundError):
        assert sha256sum("__read_a_file_not_exists__")
