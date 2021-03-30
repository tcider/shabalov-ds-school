from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def delete_node(self, node: ListNode) -> None:
        while node and node.next:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None
