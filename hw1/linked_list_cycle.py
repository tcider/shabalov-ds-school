# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        fast_ptr = head
        slow_ptr = head
        while fast_ptr:
            fast_ptr = fast_ptr.next
            if not fast_ptr:
                return False
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
            if fast_ptr == slow_ptr:
                return True
        return False
