def str_before_first(src, sub):
    """Return a substring which starts at the begin and continues to the first occurrence of the substring sub."""
    idx = src.find(sub)
    if idx < 0:
        return ""
    return src[:idx]


def str_after_first(src, sub):
    """Return a substring which starts after the first occurrence of the substring sub and continues to the end."""
    idx = src.find(sub)
    if idx < 0:
        return ""
    return src[idx+len(sub):]


def str_before_last(src, sub):
    """Return a substring which starts at the begin and continues to the last occurrence of the substring sub."""
    idx = src.rfind(sub)
    if idx < 0:
        return ""
    return src[:idx]


def str_after_last(src, sub):
    """Return a substring which starts after the last occurrence of the substring sub and continues to the end."""
    idx = src.rfind(sub)
    if idx < 0:
        return ""
    return src[idx+len(sub):]
