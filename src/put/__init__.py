# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound

from .hashutils import (
    md5str, md5sum, md5base64,
    sha1str, sha1sum, sha1base64,
    sha256str, sha256sum, sha256base64
)

from .fileutils import (
    is_file_exist,
    is_dir_exist,
    make_dir,
    join_path,
    save_json,
    load_json,
    load_lines,
    get_file_info,
    scan_dir,
)
