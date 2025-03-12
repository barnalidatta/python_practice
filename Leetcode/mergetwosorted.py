#21

class Node:
    def __init__(self, data=0) -> None:
        self.data = data
        self.next = None

def merge(L1,L2):
    head = L3 = Node()
    while L1 and L2:
        if L1.data<= L2.data:
            L3.next,L1 = L1, L1.next
        else:
            L3.next = L2
            L2 = L2.next
        L3 = L3.next
    L3.next = L1 or L2
    return head.next

def print_list(head):
    l = []
    while head:
        l.append(head.data)
        head = head.next
    print(l)

if __name__ == "__main__":
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(4)

    list2 = Node(1)
    list2.next = Node(3)
    list2.next.next = Node(4)
    print_list(list1)
    print_list(list2)
    list3 = merge(list1, list2)
    print_list(list3)
