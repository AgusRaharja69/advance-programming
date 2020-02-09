import pandas as pd

class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, data1=None, next=None):
        self.data = data
        self.data1 = data1
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def prepend(self, data,data1):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, data1=data1, next=self.head)

    def append(self, data, data1):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data, data1=data1)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data, data1=data1)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key and curr.data1 != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

    
    def listprint(self):
        printval = self.head
        while printval is not None: 
            print (str(printval.data)+";"+str(printval.data1)) #Print the node
            printval = printval.next

# defind list
list = SinglyLinkedList()

#Get data
filename = ('sepakbola-exported.csv')
arr = pd.read_csv(filename, header = None, delimiter=';')
arr = arr.values

#Making List
id = 1
for i in arr:
    if id == 1:
        list.head = ListNode(i[0],i[1])
    else:
        list.append(i[0],i[1]) 
    id += 1



print('Data Source :')
list.listprint()

