from base64 import b64encode
from functools import partial
import hashlib

_file_buffer_size = 4096


def _compute_file_hash(file_name, calc_func):
    with open(file_name, mode="rb") as f:
        d = calc_func()
        for buf in iter(partial(f.read, _file_buffer_size), b""):
            d.update(buf)
        return d


def md5str(content):
    """Calculate MD5 checksum for a string"""
    return hashlib.md5(str.encode(content)).hexdigest()


def md5sum(file_name):
    """Calculate MD5 checksum for a file"""
    return _compute_file_hash(file_name, hashlib.md5).hexdigest()


def md5base64(file_name):
    """Calculate MD5 checksum in Base64 for a file"""
    return b64encode(_compute_file_hash(file_name, hashlib.md5).digest()).decode("utf-8")


def sha1str(content):
    """Calculate SHA1 checksum for a string"""
    return hashlib.sha1(str.encode(content)).hexdigest()


def sha1sum(file_name):
    """Calculate SHA1 checksum for a file"""
    return _compute_file_hash(file_name, hashlib.sha1).hexdigest()


def sha1base64(file_name):
    """Calculate SHA1 checksum in Base64 for a file"""
    return b64encode(_compute_file_hash(file_name, hashlib.sha1).digest()).decode("utf-8")


def sha256str(content):
    """Calculate SHA256 checksum for a string"""
    return hashlib.sha256(str.encode(content)).hexdigest()


def sha256sum(file_name):
    """Calculate SHA256 checksum for a file"""
    return _compute_file_hash(file_name, hashlib.sha256).hexdigest()


def sha256base64(file_name):
    """Calculate SHA256 checksum in Base64 for a file"""
    return b64encode(_compute_file_hash(file_name, hashlib.sha256).digest()).decode("utf-8")
