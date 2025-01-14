# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # still the trick to use a dummy head to make things easier
        dummy_head = ListNode(None)
        dummy_head.next = head

        # part 1: locate the head of window
        current, left_prev = head, dummy_head
        for i in range(left - 1):
            left_prev, current = current, current.next

        # part 2: reverse the window
        prev = None 
        for i in range(right - left + 1):
            # a b -> c => a <- b  c
            next = current.next
            current.next = prev 
            prev, current = current, next

        # part 3: reconnect other parts to the reversed part
        # this is tricky without some visualization
        left_prev.next.next = current 
        left_prev.next = prev 
        
        return dummy_head.next