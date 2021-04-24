# Remove Nth Node From End of List
# medium


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # the tricky part: the head node can be removed
        # that's why we need a dummy
        dummy = ListNode(next=head)
        pointa = dummy
        pointb = dummy
        steps = 0

        while pointb != None:
            if steps < n + 1:
                # search for the nth+1 node from end
                pointb = pointb.next
                steps += 1
            else:
                # move pointer a and b together
                pointb = pointb.next
                pointa = pointa.next

        # skip the node
        pointa.next = pointa.next.next

        return dummy.next
