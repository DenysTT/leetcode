def count_uniq_values(arr):
    if len(arr) - 1  == 0:
        return 0
    elif len(arr) - 1 == 1:
        return 1
    i = 0
    used = {}
    for j, v in enumerate(arr):
        if arr[i] != v and arr[j] not in used:
            used[arr[i]] = 1
            i += 1
            arr[i] = v
    print(i + 1)


if __name__ == "__main__":
    count_uniq_values(['a','b','a','a','c']) 