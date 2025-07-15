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
        # adhoc solution

        # hash = {}

        # def traversal(node: TreeNode, level):
        #     if node != None:
        #         if level in hash:
        #             hash[level].append(node.val)
        #         else:
        #             hash[level] = [node.val]
        #         traversal(node.left, level + 1)
        #         traversal(node.right, level + 1)

        # traversal(root, 0)

        # # convert hash
        # result = []
        # for k in hash:
        #     result.append(hash[k])

        # return result

        # more standard BFS approach
        if not root:
            return []
        
        result = []
        queue = [root]  # queue for BFS, stack for DFS

        while queue:
            level_nodes = []

            # Process all nodes at the current level
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)
        
        return result

