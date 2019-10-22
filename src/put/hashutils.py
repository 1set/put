from base64 import b64encode
from functools import partial
import hashlib

FILE_BUFFER_SIZE = 4096


def _compute_file_hash(file_name, calc_func):
    with open(file_name, mode="rb") as file:
        data = calc_func()
        for buf in iter(partial(file.read, FILE_BUFFER_SIZE), b""):
            data.update(buf)
        return data


def _compute_base64_file_hash(file_name, calc_func):
    return b64encode(_compute_file_hash(file_name, calc_func).digest()).decode("utf-8")


def _compute_string_hash(content, calc_func):
    return calc_func(str.encode(content)).hexdigest()


def md5str(content):
    """Calculate MD5 checksum for a string"""
    return _compute_string_hash(content, hashlib.md5)


def md5sum(file_name):
    """Calculate MD5 checksum for a file"""
    return _compute_file_hash(file_name, hashlib.md5).hexdigest()


def md5base64(file_name):
    """Calculate MD5 checksum in Base64 for a file"""
    return _compute_base64_file_hash(file_name, hashlib.md5)


def sha1str(content):
    """Calculate SHA1 checksum for a string"""
    return _compute_string_hash(content, hashlib.sha1)


def sha1sum(file_name):
    """Calculate SHA1 checksum for a file"""
    return _compute_file_hash(file_name, hashlib.sha1).hexdigest()


def sha1base64(file_name):
    """Calculate SHA1 checksum in Base64 for a file"""
    return _compute_base64_file_hash(file_name, hashlib.sha1)


def sha256str(content):
    """Calculate SHA256 checksum for a string"""
    return _compute_string_hash(content, hashlib.sha256)


def sha256sum(file_name):
    """Calculate SHA256 checksum for a file"""
    return _compute_file_hash(file_name, hashlib.sha256).hexdigest()


def sha256base64(file_name):
    """Calculate SHA256 checksum in Base64 for a file"""
    return _compute_base64_file_hash(file_name, hashlib.sha256)
