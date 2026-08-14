# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1, v2 = 0, 0
        while l1:
            v1 = v1*10 + l1.val
            l1 = l1.next
        while l2:
            v2 = v2*10 + l2.val
            l2 = l2.next
        
        res = v1 + v2
        dummy = ListNode(0)
        res = str(res)
        cur = dummy
        for s in res:
            temp = ListNode(int(s))
            cur.next = temp
            cur = cur.next
        return dummy.next