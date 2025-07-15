def find_max(root):
    if not root:
        return float('-inf')
    
    left_max = find_max(root.left)
    right_max = find_max(root.right)
    
    return max(root.val, left_max, right_max)

def find_min(root):
    if not root:
        return float('inf')
    
    left_min = find_min(root.left)
    right_min = find_min(root.right)
    
    return min(root.val, left_min, right_min)