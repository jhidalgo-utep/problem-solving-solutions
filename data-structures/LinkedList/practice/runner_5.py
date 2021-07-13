class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head == None
        
    def insert(self, new_item):
        if LinkedList.is_empty(self):
            self.head = Node(new_item)
            self.tail = self.head
        else:
            self.tail.next = Node(new_item)
            self.tail = self.tail.next
    
    def display(self):
        if self.is_empty():
            print('empty list')
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.item)
            iter_node = iter_node.next
            

if __name__ == "__main__":
    print('starting program')
    ll = LinkedList()
    ll.insert(25)
    ll.insert(75)
    ll.insert(100)
    ll.display()