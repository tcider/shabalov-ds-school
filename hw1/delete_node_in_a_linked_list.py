# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def delete_node(self, node):
        while node and node.next:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None

        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
