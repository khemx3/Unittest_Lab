class InvalidArgument(Exception): pass


def binsearch(dataList, key):
    if type(dataList) != list:
        raise InvalidArgument("Datalist is not list")
    return _binsearch(dataList, 0, len(dataList) - 1, key)


def _binsearch(dataList, left, right, key):
    if left > right:
        return None

    mid = (left + right) // 2

    if dataList[mid] == key:
        return mid
    elif key < dataList[mid]:
        return _binsearch(dataList, left, mid - 1, key)
    else:
        return _binsearch(dataList, mid + 1, right, key)


