# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive version

        # If both nodes are None, they are the same
        if not p and not q:
            return True
        
        # If one of the nodes is None, they are not the same
        if not p or not q:
            return False
        
        # Check if the current nodes have the same value
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        # DFS version
        # stack = [(p, q)]
        # while stack:  
        #     p, q = stack.pop()
        #     if not p and not q:
        #         continue
        #     if not p or not q:
        #         return False
        #     if p.val != q.val:
        #         return False
        #     stack.append((p.left, q.left))    
        #     stack.append((p.right, q.right))
        # return True