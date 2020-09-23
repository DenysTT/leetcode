def contain_duplicate(arr):
    result = {}
    for i in arr:
        if i in result:
            return True
        else:
            result[i] = 1
    return False
