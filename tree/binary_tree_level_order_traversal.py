# medium

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        hash = {}

        def traversal(node: TreeNode, level):
            if node != None:
                if level in hash:
                    hash[level].append(node.val)
                else:
                    hash[level] = [node.val]
                traversal(node.left, level+1)
                traversal(node.right, level+1)

        traversal(root, 0)

        # convert hash
        result = []
        for k in hash:
            result.append(hash[k])

        return result



