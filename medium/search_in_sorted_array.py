def search(arr, val):
    min = 0
    max = len(arr) - 1
    while (min <= max): 
        middle = (min + max) / 2
        if arr[middle] == val:
            return val
        elif arr[middle] > val:
            max = middle + 1
        else:
            min = middle - 1




