# 19- Remobe nth node from end of the list

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def remove_nth_node(head, n):
    currentnode = head
    while(currentnode.next):
        currentnode = currentnode.next

def print_list(head):
    currentnode = head
    while currentnode:
        print(currentnode.data, end = " ")
        currentnode = currentnode.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print_list(head)
    remove_nth_node(head, n=2)
    print_list(head)
