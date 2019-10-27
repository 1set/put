from json import dumps, load, JSONEncoder
from datetime import date, datetime
from sys import version_info
from .fileutils import is_file_exist

SUPPORT_DATACLASS = version_info[0] == 3 and version_info[1] >= 7
if SUPPORT_DATACLASS:
    from dataclasses import is_dataclass, asdict


class EnhancedJSONEncoder(JSONEncoder):

    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        if SUPPORT_DATACLASS and is_dataclass(o):
            return asdict(o)
        return super().default(o)


def dump_json(obj, pretty_print=True):
    """Serialize obj to a JSON formatted string"""
    if pretty_print:
        return dumps(obj, indent=4, ensure_ascii=False, sort_keys=True, cls=EnhancedJSONEncoder)
    return dumps(obj, ensure_ascii=False, sort_keys=True, cls=EnhancedJSONEncoder)


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
