class Node:
    def __init__(self, val):
        self.val =val
        self.next=None

def check_cycle(node):
    head = node
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False    
    