# put℠

[![GitHub Action workflow](https://github.com/an63/put/workflows/build/badge.svg)](https://github.com/an63/put/actions?workflow=build)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/put?style=flat-square)](https://pypi.org/project/put/)
[![PyPI](https://img.shields.io/pypi/v/put?style=flat-square)](https://pypi.org/project/put/)
[![Project License](https://img.shields.io/pypi/l/put?style=flat-square)](https://github.com/an63/put/blob/master/LICENSE)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/put?style=flat-square)](https://pepy.tech/project/put)
[![Codacy Grade](https://img.shields.io/codacy/grade/f1c04ec78a4b45a4b8d95d89c94ba24e?style=flat-square)](https://www.codacy.com/manual/an9an63/put)
[![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability-percentage/an63/put?style=flat-square)](https://codeclimate.com/github/an63/put)
[![Codecov](https://img.shields.io/codecov/c/gh/an63/put?style=flat-square)](https://codecov.io/gh/an63/put)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light.svg)](https://deepsource.io/gh/an63/put/?ref=repository-badge)

**put**, stands for **P**ython **u**tilities & **t**ools, is a collection of wonderful Python utilities and tools that can make your life easier.

## installation

simply use pip or pipenv:

```bash
pip install put
```

## feature

the following helper methods are included:

-   **hash** utilities:
    -   md5: md5str, md5sum, md5base64
    -   sha1: sha1str, sha1sum, sha1base64
    -   sha256: sha256str, sha256sum, sha256base64

-   **file** utilities:
    -   directory: is_dir_exist, is_dir_empty, make_dir, remove_dir, scan_dir, join_path
    -   file: is_file_exist, is_file_empty, save_json, load_json, load_lines, get_file_info

-   **string** utilities:
    -   substring: str_after_first, str_after_last, str_before_first, str_before_last

-   **json** utilities:
    -   dump_json, save_json, load_json
