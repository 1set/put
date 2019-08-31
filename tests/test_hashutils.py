import pytest
from put.hashutils import md5str, md5sum, md5base64


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
