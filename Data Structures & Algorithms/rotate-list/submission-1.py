# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        size = 1 
        tail = head 
        while tail.next:
            tail = tail.next
            size += 1
            
        t = k % size
        if t == 0:
            return head
        cur = head
        for _ in range(size - t - 1):
            cur = cur.next
        
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head
