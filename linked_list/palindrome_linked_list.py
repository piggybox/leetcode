# Palindrome Linked List
# easy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pointer = head
        stack = []

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
