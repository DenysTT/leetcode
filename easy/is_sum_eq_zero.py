def is_sum_eq_zero(arr):
    pn_1 = 0
    pn_2 = len(arr) - 1 
    for i in arr:
        if arr[pn_1] + arr[pn_2] == 0:
            return True
        if arr[pn_1] + arr[pn_2] > 0:
            pn_2 -= 1
        else:
            pn_1 += 1 