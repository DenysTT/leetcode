# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        res = n = ListNode(0)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    n.next = n = ListNode(l1.val)
                    l1 = l1.next
                else:
                    n.next = n = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                n.next = n = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                n.next = n = ListNode(l2.val)
                l2 = l2.next
        return res.next