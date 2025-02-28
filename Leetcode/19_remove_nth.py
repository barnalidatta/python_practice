# 19- Remobe nth node from end of the list
# Fast and slow pointer method

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def remove_nth_node(head, n):
    currentnode = head
    # fast = currentnode.next # fast = 2
    #slow = currentnode
    
    # if currentnode.next != None:
    #     for _ in range(n):
    #         if fast.next != None:
    #             fast = fast.next
    #             print(f" fast var after running {n} loop {fast.data}")
        
    #     # fast pointer pointing to null. This is to make 
    #     # the slow pointer stop right before the node need to be removed.
    #     while fast: 
    #         fast, slow = fast.next, slow.next
    #         print(f" slow var when fast reaching NULL {slow.data}")
    #     if slow.next != None:
    #         slow.next = slow.next.next
    #     else:
    #         print("here")
    #         currentnode = slow
    #         print(slow.data)
    #         return slow
    # else:
    #     currentnode = currentnode.next
    # return currentnode
    ############################################################
    fast = currentnode
    slow = currentnode

    if currentnode.next != None:
        for _ in range(n):
            fast = fast.next
            # print(f" fast var after running {n} loop {fast.data}")
        if not fast:
            return currentnode.next
        # fast pointer pointing to null. This is to make 
        # the slow pointer stop right before the node need to be removed.
        while fast.next: 
            fast, slow = fast.next, slow.next
            print(f" slow var when fast reaching NULL {slow.data}")
            slow.next = slow.next.next
    else:
        currentnode = currentnode.next
    return currentnode


def print_list(head):
    currentnode = head
    while currentnode:
        print(currentnode.data, end = " ")
        currentnode = currentnode.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)

    # print_list(head)
    remove_nth_node(head, n=2)
    print_list(head)
