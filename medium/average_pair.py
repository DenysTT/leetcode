"""
Write a function called averagePair. Given a sorted array of integers
and a target average, determine if there is a pair of values in the array
where the average of the pair equals the target average. There may be
more than one pair that matches the average target.
Sample Input:
1 averagePair([1,2,3],2.5) // true
2 averagePair([1,3,3,5,6,7,10,12,19],8) // true
3 averagePair([-1,0,3,4,5,6], 4.1) // false
4 averagePair([],4)
"""
def average_pair(arr,v):
    p1 = 0
    p2 = len(arr) - 1
    for i in range(len(arr)):
        if p1 == p2:
            print("False")
            return False
        if (arr[p1] + arr[p2]) / 2 == v:
            print("True")
            return True
        if (arr[p1] + arr[p2]) / 2 > v:
            p2 -= 1
        else:
            p1 += 1