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
        
        res = str(v1 + v2)
        dummy = ListNode(0)
        cur = dummy
        for s in res:
            cur.next = ListNode(int(s))
            cur = cur.next
        return dummy.next