class Node(object):
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
        
    def get_next_node(self):
        return self.next
    
    def get_item(self):
        return self.item
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def set_tail_node(self, new_tail_node):
        self.tail = new_tail_node
    
    def is_empty(self):
        return self.head == None
    
    def insert(self, item):
        if LinkedList.is_empty(self):
            print('empty')
            self.head = Node(item)
            self.tail = self.head
        else:
            print('not empty')
            self.tail.next = Node(item)
            self.set_tail_node( self.tail.get_next_node() )
    
    def display(self):
        if self.is_empty():
            print("empty list to display")
        iter_node = self.head
        while iter_node != None:
            print( iter_node.get_item() )
            iter_node = iter_node.get_next_node()

        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(21)
    ll.insert(22)
    ll.display()
    