# 92
# Not Working

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Left and right are position
def reversell2(head, left, right):

    dummy_head = Node(0)
    dummy_head.next = head
    prev = dummy_head

    for _ in range(left-1):
        prev = prev.next

    curr = prev.next
    next_node = None

    print(curr.data) # 3

    for _ in range(right - left):
        temp = curr.next 
        #print(temp.data)
        curr.next = next_node
        next_node = curr
        curr = temp
        #tail.next, temp.next,prev.next = (temp.next, tail.next, temp)
    prev.next.next = curr
    prev.next = next_node
    return dummy_head.next


def print_list(head):
    l = []
    while head:
        l.append(head.data)
        head = head.next
    print(l)

if __name__ == "__main__":
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(3)
    list1.next.next.next = Node(4)
    list1.next.next.next.next = Node(5)

 
    print_list(list1)
    
    list3 = reversell2(list1,2,4)
    print_list(list3)