def str_before_first(src, trg):
    idx = src.find(trg)
    if idx < 0:
        return ""
    return src[:idx]


def str_after_first(src, trg):
    idx = src.find(trg)
    if idx < 0:
        return ""
    return src[idx+len(trg):]


def str_before_last(src, trg):
    idx = src.rfind(trg)
    if idx < 0:
        return ""
    return src[:idx]


def str_after_last(src, trg):
    idx = src.rfind(trg)
    if idx < 0:
        return ""
    return src[idx+len(trg):]
