from json import dumps, load, JSONEncoder
from datetime import date, datetime
from .fileutils import is_file_exist
from dataclasses import is_dataclass, asdict


class EnhancedJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if is_dataclass(obj):
            return asdict(obj)
        return super().default(obj)


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
