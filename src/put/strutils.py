def str_after_first(src, sub):
    """Return a substring from the first occurrence of the substring sub to the end of the string"""
    idx = src.find(sub)
    return src[idx + len(sub):] if idx >= 0 else ""


def str_after_last(src, sub):
    """Return a substring from the last occurrence of the substring sub to the end of the string"""
    idx = src.rfind(sub)
    return src[idx + len(sub):] if idx >= 0 else ""


def str_before_first(src, sub):
    """Return a substring from the beginning of the string to the first occurrence of the substring sub"""
    idx = src.find(sub)
    return src[:idx] if idx >= 0 else ""


def str_before_last(src, sub):
    """Return a substring from the beginning of the string to the last occurrence of the substring sub"""
    idx = src.rfind(sub)
    return src[:idx] if idx >= 0 else ""
