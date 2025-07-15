# medium


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
import math


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBSTMinMax(
            node: TreeNode, low=-math.inf, high=math.inf
        ):  # return flag, min, max
            if node is None:
                return True

            # check boundry
            if node.val <= low or node.val >= high:
                return False

            # for the right branch, lower bound is the current node value and higher bound is inherited
            # for the left branch, lower bound is inherited and higher bound is the current node value
            return isValidBSTMinMax(node.right, node.val, high) and isValidBSTMinMax(
                node.left, low, node.val
            )

        return isValidBSTMinMax(root)
