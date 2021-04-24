# Merge Two Sorted Lists
# easy


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2

        if l2 == None:
            return l1

        if l1.val < l2.val:
            head = l1
            p1 = l1.next
            p2 = l2
        else:
            head = l2
            p1 = l1
            p2 = l2.next

        p3 = head

        while p1 != None and p2 != None:
            if p1.val < p2.val:
                p3.next = p1
                p3 = p3.next
                p1 = p1.next
            else:
                p3.next = p2
                p3 = p3.next
                p2 = p2.next

        # finish the rest
        if p1 != None:
            p3.next = p1
        else:
            p3.next = p2

        return head