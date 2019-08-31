import pytest
from put.fileutils import is_file_exist, is_dir_exist, make_dir, save_json, load_json


def test_is_file_exist():
    assert is_file_exist("LICENSE") == True
    assert is_file_exist("tests") == False
    assert is_file_exist("__check_a_file_no_exists__") == False


def test_is_dir_exist():
    assert is_dir_exist("LICENSE") == False
    assert is_dir_exist("tests") == True
    assert is_dir_exist("__check_a_directory_no_exists__") == False


def test_make_dir():
    assert make_dir("tests") == "tests"
    assert make_dir("LICENSE") == "LICENSE"
    assert make_dir("/tmp", "py-put-test") == "/tmp/py-put-test"


def test_save_json():
    from datetime import datetime
    sample = {
        "time": datetime.now(),
        "integer": 123,
        "float": 456.789,
        "bool": True
    }
    assert save_json("/tmp/py-put-test-file.json", sample) == None
    assert save_json("/tmp/py-put-test-file2.json", sample, False) == None
    with pytest.raises(IsADirectoryError):
        assert save_json("tests", sample)


def test_load_json():
    sample = load_json("tests/resources/sample.json")
    assert sample is not None
    with pytest.raises(FileNotFoundError):
        assert load_json("__read_a_file_not_exists__")
