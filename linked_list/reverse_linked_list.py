# Reverse Linked List
# easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head 
        next = None

        # a b -> c => a <- b  c 
        while current != None :
            # keep track of the next one of current before switching
            next = current.next 

            # redirect the next pointer of current to previous
            current.next = previous 

            # move previous and current 1 step further
            previous = current
            current = next 

        return previous

