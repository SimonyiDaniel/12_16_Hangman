def get_middle(s):
    length = len(s)
    mid = length // 2

    if length % 2 != 0:
        return s[mid]

    else:
        return s[mid - 1,mid + 1]