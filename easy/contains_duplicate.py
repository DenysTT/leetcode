
"""
Implement a function called, areThereDuplicates which accepts a
variable number of arguments, and checks whether there are any
duplicates among the arguments passed in. You can solve this using
the frequency counter pattern OR the multiple pointers pattern"""
def contain_duplicate(arr):
    result = {}
    for i in arr:
        if i in result:
            return True
        else:
            result[i] = 1
    return False

def are_there_duplicates(arr):
    arr.sort()
    pointer = 1
    for i in range(len(arr) - 1):
        if arr[i] == arr[pointer]:
            print("yaas")
            return True
        pointer += 1
