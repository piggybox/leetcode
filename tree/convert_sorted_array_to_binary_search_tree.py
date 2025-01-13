# easy

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # devide and conqure
        if len(nums) == 0:
            return None 
        else:
            mid = len(nums) // 2
            node = TreeNode()
            node.val = nums[mid]
            node.left = self.sortedArrayToBST(nums[0:mid])
            node.right = self.sortedArrayToBST(nums[mid:len(nums)])

            return node
