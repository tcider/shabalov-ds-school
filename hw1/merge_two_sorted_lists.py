# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            list_head = l1
            l1 = l1.next
        else:
            list_head = l2
            l2 = l2.next
        list_iter = list_head
        while l2 and l1:
            if l2.val > l1.val:
                list_iter.next = l1
                l1 = l1.next
            else:
                list_iter.next = l2
                l2 = l2.next
            list_iter = list_iter.next
        if l1:
            list_iter.next = l1
        elif l2:
            list_iter.next = l2
        else:
            list_iter.next = None
        return list_head
