# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    def get_next_node(self):
        return self.next
    
    def get_node_data(self):
        return self.data
    
    def set_next_node(self, insert_node):
        self.next = insert_node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, insert_data):
        if self.head == None:
            self.head = Node(insert_data)
            self.tail = self.head
        else:
            Node.set_next_node( self.tail, Node(insert_data) )
            self.tail = Node.get_next_node( self.tail )
    
    def print_list(self):
        if self.head == None:
            return
        iter_node = self.head
        while iter_node != None:
            print( Node.get_node_data(iter_node) )
            iter_node = Node.get_next_node(iter_node)

def main():
    print('start main:')
    
    my_list = LinkedList()
    my_list.insert(23)
    my_list.insert(45)
    my_list.insert(81)
    my_list.print_list()
    

#checks value of name and compares it to string main
if __name__ == "__main__":
    print('program start:\n')
    main()
    

    