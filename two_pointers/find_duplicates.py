class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # although the input is a list of integers, we can treat it as a linked list
        # where each number points to the index of the next number
        # since the numbers are in the range [1, n], we can use the numbers
        # as indices to traverse the list

        # Using Floyd's Tortoise and Hare (Cycle Detection)
        slow = nums[0]
        fast = nums[0]

        # First phase: Finding the intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break   

        # Second phase: Finding the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
    
        return slow
    