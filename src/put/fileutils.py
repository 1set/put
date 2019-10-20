from datetime import date, datetime
from glob import iglob
from json import dump, load
from pathlib import Path
from .hashutils import md5sum, md5base64
import errno
import os


def is_file_exist(file_path):
    """Whether the file exists"""
    file_path_info = Path(file_path)
    return file_path_info.is_file()


def is_dir_exist(file_path):
    """Whether the directory exists"""
    file_path_info = Path(file_path)
    return file_path_info.is_dir()


def make_dir(*args):
    """Create a directory with named path if not exists"""
    path = os.path.join(*args)
    try:
        os.makedirs(path)
    except OSError as ex:
        if ex.errno != errno.EEXIST or not is_dir_exist(path):
            raise
    return path


def join_path(*args):
    """Join two or more or less paths"""
    return os.path.join(*args)


def _json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def save_json(file_path, data, pretty_print=True):
    """Serialize data and save as JSON file"""
    with open(file_path, "w", encoding="utf8") as outfile:
        if pretty_print:
            dump(
                data,
                outfile,
                ensure_ascii=False,
                sort_keys=True,
                indent=4,
                default=_json_serial,
            )
        else:
            dump(data, outfile, ensure_ascii=False, default=_json_serial)


def load_json(file_path):
    """Load JSON file and deserialize"""
    if is_file_exist(file_path):
        with open(file_path, "r") as infile:
            data = load(infile)
            return data
    else:
        return None


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


def _is_file_type_match(path_str, file_ext):
    if file_ext is None:
        return True
    path_str = path_str.lower()
    for ext in file_ext:
        if path_str.endswith(ext):
            return True
    return False


def scan_dir(src_dir, file_ext_names=None, calc_hash=False, recursive=True):
    """Walk through the directory recursively and retrieve all the file info"""
    if recursive:
        path_suffix = "/**/*"
    else:
        path_suffix = "/**"
    file_ext = None if file_ext_names is None else ["." + ext.lstrip(".") for ext in file_ext_names if len(ext) > 0]
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
