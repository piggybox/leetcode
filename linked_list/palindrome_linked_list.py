# Palindrome Linked List
# easy

from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pointer = head
        stack = deque() # more efficient than list

        # push to stack
        while pointer != None:
            stack.append(pointer.val)
            pointer = pointer.next

        # check the list against the stack
        pointer = head
        while pointer != None:
            if pointer.val == stack.pop():
                pointer = pointer.next
                continue
            else:
                return False

        return True

        # alternative solution to find the mid point of linked list
        # then compare two halves, pretty complicated