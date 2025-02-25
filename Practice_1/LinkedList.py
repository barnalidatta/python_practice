# 83. Remove Duplicates from Sorted List
# 82. Remove Duplicates from Sorted List2 (leaving only distinct numbers)
# 61. Rotate List
# TWO POINTER/ITERATOR PATTERN BECAUSE LIST IS SORTED
# Definition for singly-linked list.

# while current:

# This is what you use when you want to potentially process all nodes in the loop, 
# and have no need to still have access to the last node once the loop finishes. 
# After the loop finishes, current will be None.

# while current.next:

# This is what you use when you want to find the last node in the list. 
# After the loop finishes, current will be that final node. 
# So this loop stops one step earlier than the other one. 
# But there is a precaution to take: if current is None at the start of the loop, 
# there will be an exception. So only use this when you are already sure that current is not None.

class Node(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insertend(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        else:
            currentnode = self.head
            while(currentnode.next):
                currentnode = currentnode.next
            currentnode.next = newnode

    def printll(self):
        currentnode = self.head
        while(currentnode):
            print(currentnode.data)
            currentnode = currentnode.next


#class Solution(object):
    def deleteDuplicates(self):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if self.head == None:
            return
        current_node = self.head
        while (current_node):
            next_node = current_node.next
            while next_node and next_node.data == current_node.data:
                next_node = next_node.next
            # Update current_node.next address part beacuse next_node might got removed.
            current_node.next = next_node
            current_node = next_node

    def deleteDuplicates2(self):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_node = Node(0)
        dummy_node.next = self.head
        prev = dummy_node
        current_node = self.head

        while current_node:
            print(f'current node {current_node.data}')
            if current_node.next and current_node.data == current_node.next.data:
                while current_node.next and current_node.data == current_node.next.data:
                    current_node = current_node.next
                prev.next = current_node.next
            else:
                prev = current_node
                print(f'prev data {prev.data}')
            current_node = current_node.next
        if dummy_node.next:
            print(f'dummy next data {dummy_node.next.data}')
        if self.head:
            print(f'self head data {self.head.data}')
        self.head = dummy_node.next

    def rotate_list_debug(self):
        circ_head = self.head
        
        if self.head == None:
            return
        current_node = self.head
        # getting the size. 
        # Check the difference between while loops current_node and current_node.next
        le,l = 0,0
        while current_node:
            le = le+1
            print(f'current node is {current_node.data}') # Output : 1,2,3,4,5
            current_node = current_node.next           
        print(f'length is {le}') # Output is 5 for 5 elements
        # Resetting current_node to head
        current_node = self.head
        # Make it circular. Traverse till last node
        while current_node.next:
            l = l+1  
            print(f'current node next loop is {current_node.data}') # Output : 1,2,3,4
            current_node = current_node.next
        print(f'length : {l}') # Output: 4 for 5 elements
        if current_node:
            print(f'current node after next loop finishes is {current_node.data}') # Output : 5
        if current_node and circ_head:
                if current_node.next == None:
                    current_node.next = circ_head
                print(f'current node should be 5 : {current_node.data}')
                print(f'head should be 1 : {circ_head.data}')
        pos = 0
        # if current_node.next:
        #     print(f'current node next data should point to head and value 1 {current_node.next.data}')

        # traverse list till totalelement - number of given place to move -1 , -1 for one node before new_head
        while circ_head and pos != 3-1:
            pos = pos +1
            circ_head = circ_head.next
        # Just to print. Delete later
        if circ_head:
            print(f'head should be 3 : {circ_head.data}')    
        # save the node before new head 
        prev = circ_head
        # go to the new head and make previous node address none.
        if circ_head and prev:
            circ_head = circ_head.next
            prev.next = None
        self.head = circ_head 
        return circ_head

    def rotate_list_change(self, k=2):
        circ_head = self.head    
        if self.head == None:
            return
        current_node = self.head
        leng=1
        # get the length
        while current_node.next:
            leng = leng+1          
            current_node = current_node.next
        print(f'length is {leng}')   
        # if current_node and circ_head:
        #         if current_node.next == None:

        # make it circular
        current_node.next = circ_head

        pos = leng-k-1 # 2
        current_node = circ_head # current_node :1
        for _ in range (pos):
            current_node = current_node.next
        print(f'current node {current_node.data}')
        # while circ_head and pos != leng-k-1:
        #     pos = pos +1
        #     circ_head = circ_head.next
         
        #prev = circ_head
        # save the node before head
        #prev = current_node
        # go to the next node
        new_head = current_node.next
        print(f'new head should be 4 : {new_head.data}')
        current_node.next = None
        # if circ_head and prev:
        #     circ_head = circ_head.next
        #     prev.next = None
        self.head = new_head 
        return new_head

    def rotate_list(self, k=2):
        circ_head = self.head    
        if self.head == None:
            return
        current_node = self.head
        leng=1
        # get the length
        while current_node.next:
            leng = leng+1          
            current_node = current_node.next
        print(f'length is {leng}')   

        # make it circular
        current_node.next = circ_head
        # update the current node
        current_node = circ_head # current_node :1
        # go to one node before new head (calculate based on place)
        pos = leng-k-1 # 2 
        for _ in range (pos):
            current_node = current_node.next
        # current_node is one node before
        new_head = current_node.next
        current_node.next = None
        self.head = new_head 
        return new_head

    def rotate_leet(self,k=2):
            
        if k ==0 or self.head == None:
            return self.head
        current_node = self.head
        ohead = self.head
        leng=1
        # get the length
        while current_node.next:
            leng = leng+1          
            current_node = current_node.next
        
        k %= leng
        print(f'k is {k}')
            
        if k ==0:
            return self.head
        # circular
        current_node.next = self.head
        print(f'Current node is {current_node.data}')
        # update current node
        #current_node = self.head
        # go to one node before new head (calculate based on place) 
        for _ in range (1,k):
            current_node = current_node.next
            print(f'Current node is {current_node.data}')
        # current_node is one node before
        new_head = current_node.next
        print(f'new head is {new_head.data}')
        current_node.next = None  
        self.head = new_head
        


if __name__ =='__main__':
    ll = LinkedList()
    ll.insertend(1)
    ll.insertend(2)
    ll.insertend(3)
    # ll.insertend(3)
    # #ll.insertend(4)
    # ll.insertend(4)
    # ll.insertend(5)
    
    ll.printll()
    # print(f'delete duplicates')
    # ll.deleteDuplicates()
    # ll.printll()
    # print(f'delete duplicates2')
    # ll.deleteDuplicates2()
    # ll.printll()
    print(f'Rotate list')
    #ll.rotate_list()
    ll.rotate_leet()
    ll.printll()