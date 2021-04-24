# Linked List Cycle
# easy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = head  # slow pointer
        p2 = head  # faster pointer

        cycle = False 

        while p1 != None and p2 != None and p2.next != None :
            p2 = p2.next.next
            p1 = p1.next 

            if p1 == p2:
                cycle = True
                break


        return cycle