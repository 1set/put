from json import dumps, load
from datetime import date, datetime
from .fileutils import is_file_exist


def _json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def dump_json(obj, pretty_print=True, ignore_error=False):
    """Serialize obj to a JSON formatted string"""
    if pretty_print:
        return dumps(obj, indent=4, ensure_ascii=False, sort_keys=True, skipkeys=ignore_error, default=_json_serial)
    return dumps(obj, ensure_ascii=False, sort_keys=True, skipkeys=ignore_error, default=_json_serial)


def save_json(file_path, data, pretty_print=True):
    """Serialize data and save as JSON file"""
    with open(file_path, "w", encoding="utf8") as outfile:
        outfile.write(dump_json(data, pretty_print))


def load_json(file_path):
    """Load JSON file and deserialize"""
    if is_file_exist(file_path):
        with open(file_path, "r") as infile:
            data = load(infile)
            return data
    else:
        return None
