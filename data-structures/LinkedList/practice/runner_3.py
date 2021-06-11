class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        

if __name__ == "__main__":
    my_list = LinkedList()