#141

class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next=None

# Floyd’s Cycle-Finding Algorithm – O(n) Time and O(1) Space
# two pointers running in a circular loop will catchup each other
# doesn't matter where. ie if these two pointer catchup means there
# is a circle
# 40ms
def checkloop2(head):
    slow = fast = head
    while slow and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            print("Circle Found")
            return True
    return False

# Naive approach - Hashset - O(n) Time and O(n) Space
# 800ms
def checkloop(head):
    currentnode = head
    elements = []
    # address = []
    address = set()
    while True:
        elements.append(currentnode.data)
        # address.append(currentnode) 
        address.add(currentnode)       
        if currentnode.next in address:
            print(currentnode.data)
            break
        currentnode = currentnode.next
    print(f"Elements in LL are {elements}")

if __name__ == "__main__":
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(-4)

    last = node.next.next.next
    last.next = node
    checkloop(node)
    checkloop2(node)