# DFS
# just for familiarity not explored deeply, 
def max_depth(root):
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1+max(left_depth,right_depth)