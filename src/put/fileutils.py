from glob import iglob
from pathlib import Path
from shutil import rmtree
from datetime import datetime
from .hashutils import md5sum, md5base64
import errno
import os


def join_path(*args):
    """Join two or more or less paths"""
    return os.path.join(*args)


def is_file_exist(path):
    """Whether the file exists"""
    path_info = Path(path)
    return path_info.is_file()


def is_dir_exist(path):
    """Whether the directory exists"""
    path_info = Path(path)
    return path_info.is_dir()


def is_dir_empty(path):
    """Whether the directory is empty"""
    return is_dir_exist(path) and not os.listdir(path)


def is_file_empty(path):
    """Whether the file is empty"""
    return is_file_exist(path) and os.stat(path).st_size == 0


def make_dir(path):
    """Create a directory with named path if not exists"""
    try:
        os.makedirs(path)
    except OSError as ex:
        if ex.errno != errno.EEXIST or not is_dir_exist(path):
            raise
    return path


def remove_dir(path):
    """Remove a directory whether it is empty or not"""
    rmtree(path, ignore_errors=True)


def load_lines(file_path):
    """Load all lines from text file"""
    if is_file_exist(file_path):
        with open(file_path, "r") as infile:
            data = list(map(lambda l: l.rstrip(), infile.readlines()))
            return data
    else:
        return None


def get_file_info(path_str, calc_hash=False):
    """Retrieve file info and calculate file hash if required"""
    stat_info = os.stat(path_str)
    stat_size = stat_info.st_size
    file_date = datetime.utcfromtimestamp(stat_info.st_mtime)
    file_name = os.path.basename(path_str)
    name_parts = os.path.splitext(file_name)
    return {
        "name": file_name,
        "path": path_str,
        "base": name_parts[0],
        "extn": name_parts[1].lstrip("."),
        "dirn": os.path.basename(os.path.dirname(path_str)),
        "size": stat_size,
        "hash": md5sum(path_str) if calc_hash else None,
        "bmd5": md5base64(path_str) if calc_hash else None,
        "time": file_date,
    }


def _is_file_type_match(path_str, file_ext):
    if file_ext is None:
        return True
    path_str = path_str.lower()
    for ext in file_ext:
        if path_str.lower().endswith(ext):
            return True
    return False


def scan_dir(src_dir, file_ext_names=None, calc_hash=False, recursive=True):
    """Walk through the directory recursively and retrieve all the file info"""
    if recursive:
        path_suffix = "/**/*"
    else:
        path_suffix = "/**"
    file_ext = None
    if file_ext_names is not None:
        file_ext = ["." + ext.lstrip(".").lower() for ext in file_ext_names if ext]
    file_list = [
        f for f in iglob(src_dir + path_suffix, recursive=recursive) if os.path.isfile(f) and _is_file_type_match(f, file_ext)
    ]
    stat_list = []
    for file in file_list:
        file_info = get_file_info(file, calc_hash)
        if file_info:
            stat_list.append(file_info)
    stat_list.sort(key=lambda p: p["name"])
    return stat_list
