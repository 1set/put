from base64 import b64encode, b32encode
from datetime import date, datetime
from glob import iglob
from functools import partial
from json import dump, load
from pathlib import Path
import errno
import hashlib
import os


def make_directory(*args):
    """Create a directory with named path if not exists"""
    path = os.path.join(*args)
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return path


def _json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def save_json(file_path, data):
    """Serialize data and save as JSON file"""
    with open(file_path, "w", encoding="utf8") as outfile:
        dump(
            data,
            outfile,
            ensure_ascii=False,
            sort_keys=True,
            indent=4,
            default=_json_serial,
        )


def load_json(file_path):
    """Load JSON file and deserialize"""
    with open(file_path, "r") as infile:
        data = load(infile)
        return data


def _compute_md5_hash(file_name):
    with open(file_name, mode="rb") as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 4096), b""):
            d.update(buf)
        return d


def md5sum(file_name):
    return _compute_md5_hash(file_name).hexdigest()


def md5base64(file_name):
    return b64encode(_compute_md5_hash(file_name).digest()).decode("utf-8")


def md5str(content):
    return (
        b32encode(hashlib.md5(str.encode(content)).digest()).decode("utf-8").rstrip("=")
    )


def _is_file_type_match(path_str, file_ext):
    path_str = path_str.lower()
    for ext in file_ext:
        if path_str.endswith(ext):
            return True
    return False


def get_file_info(path_str, calc_hash=False):
    stat_info = os.stat(path_str)
    stat_size = stat_info.st_size
    file_date = datetime.utcfromtimestamp(stat_info.st_mtime)
    file_name = os.path.basename(path_str)
    return {
        "name": file_name,
        "path": path_str,
        "base": os.path.splitext(file_name)[0],
        "dirn": os.path.basename(os.path.dirname(path_str)),
        "size": stat_size,
        "hash": md5sum(path_str) if calc_hash else None,
        "bmd5": md5base64(path_str) if calc_hash else None,
        "time": file_date,
    }


def scan_directory(source_directory, file_ext_names, calc_hash=False):
    file_list = [
        f
        for f in iglob(source_directory + "/**/*", recursive=True)
        if os.path.isfile(f) and _is_file_type_match(f, file_ext_names)
    ]
    stat_list = []
    for file in file_list:
        file_info = get_file_info(file, calc_hash)
        if file_info:
            stat_list.append(file_info)
    stat_list.sort(key=lambda p: p["name"])
    return stat_list


def is_file_exist(file_path):
    file_path_info = Path(file_path)
    return file_path_info.is_file()


def is_dir_exist(file_path):
    file_path_info = Path(file_path)
    return file_path_info.is_dir()
