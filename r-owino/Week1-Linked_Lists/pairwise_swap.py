#!/usr/bin/env python3
"""
24. Swap Nodes in Pairs

Example:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
given: 1 -> 2 -> 3 -> 4
swap: 2 -> 1 -> 4 -> 3

Input: head = [1,2,3]
Output: [2,1,3]
given: 1 -> 2 -> 3
swap: 2 -> 1 -> 3
"""

from typing import Optional
from reverse_list import linked_list_to_list, list_to_linked_list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(0, 1)
        dummy.next = head

        curr = dummy

        # check that the nodes to be swapped are not null
        while curr.next is not None and curr.next.next is not None:
            # identify nodes to swap
            swap1 = curr.next
            swap2 = curr.next.next

            # actual swap
            swap1.next = swap2.next
            swap2.next = swap1

            # next pair swap
            curr.next = swap2
            curr = swap1
        
        return dummy.next

sol = Solution()
linked_list = list_to_linked_list([4])
print(linked_list_to_list(sol.swapPairs(linked_list)))
