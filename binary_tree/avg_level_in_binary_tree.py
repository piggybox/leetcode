# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []
        queue = [root] # queue for BFS, stack for DFS

        # Perform level order traversal
        while queue:
            level_sum = 0
            level_count = len(queue)

            # Process all nodes at the current level
            for _ in range(level_count): 
                node = queue.pop(0)
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_count)

        return result