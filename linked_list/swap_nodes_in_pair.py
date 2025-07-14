# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify edge cases!
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Traverse the list in pairs
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            # Swap the nodes
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev to the next pair
            prev = first
        
        return dummy.next    