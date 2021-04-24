# easy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
            
        if root.left != None:
            depth_left = 1 + self.maxDepth(root.left)
        else:
            depth_left = 1

        if root.right != None:
            depth_right = 1 + self.maxDepth(root.right)
        else:
            depth_right = 1

        return max(depth_right, depth_left)