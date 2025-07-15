# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # If one of the children is None, return the depth of the other child plus one
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # If both children exist, return the minimum depth of the two children plus one for the current node
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))