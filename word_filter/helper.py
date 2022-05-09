def iscollection(obj):
    col = getattr(obj, '__getitem__', False)
    val = False if (not col) else True

    if isstring(obj):
        val = False

    return val


def isstring(obj):
    return True if type(obj).__name__ == 'str' else False


def enc(str):
    return str.encode('ascii', 'ignore')


def dec(str):
    return str.decode('ascii', 'ignore')
