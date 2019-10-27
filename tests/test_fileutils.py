# -*- coding: UTF-8 -*-

import pytest
from put.fileutils import (
    is_file_exist,
    is_file_empty,
    is_dir_exist,
    is_dir_empty,
    make_dir,
    remove_dir,
    join_path,
    load_lines,
    get_file_info,
    scan_dir,
)
from tempfile import TemporaryDirectory


def test_is_file_exist():
    assert is_file_exist("LICENSE")
    assert not is_file_exist("__check_a_file_not_exists__")
    assert not is_file_exist("tests")
    assert not is_file_exist(join_path("tests", "resources"))
    assert is_file_exist(join_path("tests", "resources", "sample.json"))


def test_is_file_empty():
    assert not is_file_empty("LICENSE")
    assert not is_file_exist("__check_a_file_not_exists__")
    assert not is_file_empty("tests")
    assert not is_file_empty(join_path("tests", "resources"))
    assert not is_file_empty(join_path("tests", "resources", "sample.json"))
    assert is_file_empty(join_path("tests", "resources", "empty.file"))


def test_is_dir_exist():
    assert not is_dir_exist("LICENSE")
    assert is_dir_exist("tests")
    assert not is_dir_exist("__check_a_directory_not_exists__")
    assert is_dir_exist(join_path("tests", "resources"))
    assert not is_dir_exist(join_path("tests", "resources", "sample.json"))


def test_is_dir_empty():
    assert not is_dir_empty("LICENSE")
    assert not is_dir_empty("tests")
    assert not is_dir_empty(join_path("tests", "resources"))
    assert not is_dir_empty("__check_a_directory_not_exists__")
    with TemporaryDirectory() as tmp_dir:
        assert is_dir_empty(tmp_dir)
        dir_path = join_path(tmp_dir, "nested-empty")
        make_dir(dir_path)
        assert is_dir_empty(dir_path)
        assert not is_dir_empty(join_path(dir_path, "__nested_not_exists__"))


def test_make_dir():
    assert make_dir("tests") == "tests"
    with TemporaryDirectory() as tmp_dir:
        target_dir = join_path(tmp_dir, "py-put-test-make")
        assert make_dir(target_dir) == target_dir
        assert is_dir_exist(target_dir)
        target_dir = join_path(tmp_dir, "py-put-test-makeq", "123", "456", "789")
        assert make_dir(target_dir) == target_dir
        assert is_dir_exist(target_dir)
    with pytest.raises(FileExistsError):
        assert make_dir("LICENSE") == "LICENSE"


def test_remove_dir():
    assert remove_dir("__remove_a_directory_no_exists__") is None
    target_file = "LICENSE"
    assert is_file_exist(target_file)
    assert remove_dir(target_file) is None
    assert is_file_exist(target_file)
    with TemporaryDirectory() as tmp_dir:
        target_dir = join_path(tmp_dir, "py-put-test-remove")
        assert make_dir(target_dir) == target_dir
        assert is_dir_exist(target_dir)
        assert remove_dir(target_dir) is None
        assert not is_dir_exist(target_dir)


def test_join_path():
    assert join_path("") == ""
    assert join_path("hello") == "hello"
    assert join_path("hello", "world") == "hello/world"
    assert join_path("a", "b", "c") == "a/b/c"
    with pytest.raises(TypeError):
        assert join_path()


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
    assert info1["dirn"] == "resources"
    assert info1["base"] == "sample"
    assert info1["extn"] == "json"
    assert info1["size"] == 104
    assert info1["hash"] is None
    assert info1["bmd5"] is None
    info2 = get_file_info("tests/resources/sample.json", True)
    assert info2 is not None
    assert info2["name"] == "sample.json"
    assert info2["size"] == 104
    assert info2["hash"] == "5983c06a82baabe47239ca1502291f54"
    assert info2["bmd5"] == "WYPAaoK6q+RyOcoVAikfVA=="
    info3 = get_file_info("tests/test_fileutils.py", True)
    assert info3["dirn"] == "tests"
    assert info3["name"] == "test_fileutils.py"
    assert info3["base"] == "test_fileutils"
    assert info3["extn"] == "py"


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
    files10 = scan_dir("tests", ["PY", "JSON"], True)
    assert len(files10) >= 1
