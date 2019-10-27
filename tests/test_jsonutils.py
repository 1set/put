# -*- coding: UTF-8 -*-

import pytest
from put.jsonutils import (
    save_json,
    load_json,
)
from put.fileutils import join_path
from datetime import datetime
from tempfile import TemporaryDirectory


def test_save_json():
    sample = {"time": datetime.now(), "integer": 123, "float": 456.789, "bool": True}
    with TemporaryDirectory() as tmp_dir:
        assert save_json(join_path(tmp_dir, "py-put-test-file.json"), sample) is None
        assert save_json(join_path(tmp_dir, "py-put-test-file2.json"), sample, False) is None
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
