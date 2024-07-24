class ListNode(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next != None:
            current_node= current_node.next
        current_node.next = new_node
        #new_node.next = None

        # print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

llist = LinkedList()    

llist.insertAtEnd('a')
llist.insertAtEnd('b') 
llist.printLL()
