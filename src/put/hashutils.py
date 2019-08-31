from base64 import b64encode, b32encode
from functools import partial
import hashlib


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
