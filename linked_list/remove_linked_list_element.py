# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # the tricky part is to cover edge cases
        
        # creating dummy in case the first node gets removed
        dummy_head = ListNode(None)
        dummy_head.next = head
        current = dummy_head
        
        # another trick is to only use one pointer, not (previous, current)
        while current.next != None:
            if current.next.val == val:
                # remove current.next node 
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy_head.next