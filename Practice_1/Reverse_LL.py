# pyright: reportAttributeAccessIssue=false

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def reverse_ll(node):
    head = node
    
    prev = None
    curr = head

    while curr:
        nxt = curr.next # save the next address of current node
        curr.next = prev # update the next address of current node. Arrow reverse
        prev = curr      #  move up the prev
        curr = nxt      # update the curr
    return prev
    

def print_node(node):
    head = node
    while head != None:
        print(head.val)
        head = head.next

head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.next = node3

print_node(head)
l = reverse_ll(head)
print_node(l)
