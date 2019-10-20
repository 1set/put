import pytest
from put.fileutils import (
    is_file_exist,
    is_dir_exist,
    make_dir,
    join_path,
    save_json,
    load_json,
    load_lines,
    get_file_info,
    scan_dir,
)
from datetime import date, datetime


def test_is_file_exist():
    assert is_file_exist("LICENSE")
    assert not is_file_exist("tests")
    assert not is_file_exist("__check_a_file_no_exists__")


def test_is_dir_exist():
    assert not is_dir_exist("LICENSE")
    assert is_dir_exist("tests")
    assert not is_dir_exist("__check_a_directory_no_exists__")


def test_join_path():
    assert join_path("") == ""
    assert join_path("hello") == "hello"
    assert join_path("hello", "world") == "hello/world"
    assert join_path("a", "b", "c") == "a/b/c"
    with pytest.raises(TypeError):
        assert join_path()


def test_make_dir():
    assert make_dir("tests") == "tests"
    assert make_dir("/tmp", "py-put-test") == "/tmp/py-put-test"
    with pytest.raises(FileExistsError):
        assert make_dir("LICENSE") == "LICENSE"


def test_save_json():
    sample = {"time": datetime.now(), "integer": 123, "float": 456.789, "bool": True}
    assert save_json("/tmp/py-put-test-file.json", sample) is None
    assert save_json("/tmp/py-put-test-file2.json", sample, False) is None
    with pytest.raises(IsADirectoryError):
        assert save_json("tests", sample)


def test_load_json():
    sample = load_json("tests/resources/sample.json")
    assert sample is not None
    assert sample["integer"] == 123
    assert sample["bool"]
    assert load_json("__read_a_file_not_exists__") is None
    with pytest.raises(UnicodeDecodeError):
        assert load_json("tests/resources/sample.zip")


def test_load_lines():
    sample = load_lines("tests/resources/sample.json")
    assert sample is not None
    assert len(sample) == 6
    assert load_lines("__read_a_file_not_exists__") is None
    with pytest.raises(UnicodeDecodeError):
        assert load_lines("tests/resources/sample.zip")


def test_get_file_info():
    info1 = get_file_info("tests/resources/sample.json")
    assert info1 is not None
    assert info1["name"] == "sample.json"
    assert info1["size"] == 104
    assert info1["hash"] is None
    assert info1["bmd5"] is None
    info2 = get_file_info("tests/resources/sample.json", True)
    assert info2 is not None
    assert info2["name"] == "sample.json"
    assert info2["size"] == 104
    assert info2["hash"] == "5983c06a82baabe47239ca1502291f54"
    assert info2["bmd5"] == "WYPAaoK6q+RyOcoVAikfVA=="


def test_scan_dir():
    files1 = scan_dir("tests", ["json"])
    assert len(files1) >= 1
    assert len([f for f in files1 if f["name"].endswith("json")]) == len(files1)
    files2 = scan_dir("tests", [".json"])
    assert len(files2) >= 1
    assert len([f for f in files2 if f["name"].endswith(".json")]) == len(files2)
    files3 = scan_dir("tests", ["py"], True)
    assert len(files3) >= 1
    assert len([f for f in files3 if f["name"].endswith("py")]) == len(files3)
    assert len([f for f in files3 if f["hash"] is not None]) == len(files3)
    files4 = scan_dir("tests")
    assert len(files4) >= 1
    files5 = scan_dir("tests", [])
    assert len(files5) == 0
    files6 = scan_dir("tests", ["py", "json"])
    assert len([f for f in files6 if f['dirn'] == "resources"]) >= 1
    files7 = scan_dir("tests", ["py", "json"], recursive=False)
    assert len([f for f in files7 if f['dirn'] == "resources"]) == 0
    files8 = scan_dir("tests", ["py", "json"])
    assert len([f for f in files8 if not (f['hash'] is None and f['bmd5'] is None)]) == 0
    files9 = scan_dir("tests", ["py", "json"], calc_hash=True)
    assert len([f for f in files9 if f['hash'] is None or f['bmd5'] is None]) == 0
