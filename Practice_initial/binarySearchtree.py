# A Binary search tree is a tree that follows some order to arrange the elements, 
# whereas the binary tree does not follow any order. In a Binary search tree, the
# value of the left node must be smaller than the parent node, and the value of the
# right node must be greater than the parent node.

def build_bst(sorted_list):
    if len(sorted_list) == 0:
        return "empty"
    middle_index = len(sorted_list)//2
    middle_value = sorted_list[middle_index]

    node = {"data":middle_value}
    node["left"] = build_bst(sorted_list[:middle_index])
    node["right"] = build_bst(sorted_list[middle_index+1 :])

    return node


sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

