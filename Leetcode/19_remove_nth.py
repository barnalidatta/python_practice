# 19- Remobe nth node from end of the list
# Fast and slow pointer method

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def remove_nth_node(head, n):
    currentnode = head
    fast = currentnode.next # fast = 2
    slow = currentnode
    
    if currentnode.next != None:
        # fast pointer to point to 6th node if n=5 as fast
        # started from 2nd node in this loop
        for _ in range(n):
            if fast != None:
                fast = fast.next
                #print(f" fast var after running {n} loop {fast.data}")
        # fast pointer pointing to null. This is to make 
        # the slow pointer stop right before the node need to be removed.
        # while fast is not NULL
        while fast: 
            fast, slow = fast.next, slow.next
            print(f"\nslow var when fast reaching NULL {slow.data}")
        if slow.next != None:
            slow.next = slow.next.next
        else:
            print("\nDeleting the first node")
            currentnode = slow
            return slow
    else:
        # here when current node is the only node, List has 1 ele
        print("\nOne element")
        currentnode = currentnode.next
    # Below print fails when list has one node and n=1
    #print(head.data)
    return currentnode
    ############################################################
    # Below code works on Leetcode for Input = [1,2], n=1 and 
    # Input = [1], n=1
    # But not here

    # fast = currentnode
    # slow = currentnode

    # if currentnode.next != None:
    #     # fast pointer to point to 5th element if n=5
    #     for _ in range(n):
    #         fast = fast.next
    #         # print(f" fast var after running {n} loop {fast.data}")
    #     if not fast:
    #         return currentnode.next
    #     # fast pointer pointing to null. This is to make 
    #     # the slow pointer stop right before the node need to be removed.
    #     while fast.next: 
    #         fast, slow = fast.next, slow.next
    #         print(f" slow var when fast reaching NULL {slow.data}")
    #         slow.next = slow.next.next
    # else:
    #     currentnode = currentnode.next
    # return currentnode


def print_list(head):
    currentnode = head
    list_format = []
    while currentnode:
        list_format.append(currentnode.data)
        #print(f"\nlist of nodes {currentnode.data}", end = " ")
        currentnode = currentnode.next
    print(f"Current nodes : {list_format}")
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)
    n = 2
    print_list(head)
    head = remove_nth_node(head, n)
    print(f"\nAfter removing {n} from last node")
    print_list(head)
