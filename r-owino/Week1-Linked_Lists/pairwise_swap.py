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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        # check that the nodes to be swapped are not null
        while curr.next and curr.next.next:
            # identify nodes to swap
            first = curr.next
            second = first.next

            # actual swap
            first.next = second.next
            second.next = first
            curr.next = second

            # next pair swap
            curr = first
        
        return dummy.next
    
    def insert_node(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def dislay(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.val)
            current = current.next
        print(" -> ".join(map(str, nodes)))

if __name__ == "__main__":
    sol = Solution()
    sol.insert_node(1)
    sol.insert_node(2)
    # sol.insert_node(3)
    # sol.insert_node(4)
    # sol.insert_node(6)

    # display the inserted list
    print("Original list:")
    sol.dislay()

    # swap pairs
    sol.head = sol.swapPairs(sol.head)
    
    # display list after swapping
    print("After swapping:")
    sol.dislay()
