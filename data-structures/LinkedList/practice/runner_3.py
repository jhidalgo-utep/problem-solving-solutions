class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    #Self parameter is the Node object/class
    def get_next_node(self):
        return self.next
    
    def get_node_data(self):
        return self.data

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    #Self parameter is the linkedlist obj
    def insert(self, insert_data):
        if self.head == None:
            self.head = Node(insert_data)
            self.tail = self.head
        else:
            self.tail.next = Node(insert_data)
            self.tail = self.tail.next
    
    def print_list(self):
        if self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print(iter_node.get_node_data() )
            iter_node = iter_node.get_next_node()
    
    
        

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.insert(33)
    my_list.insert(34)
    my_list.insert(35)
    my_list.insert(36)
    
    my_list.print_list()