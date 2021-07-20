# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:56:46 2021

@author: joaqu
"""

class HashMap(object):
    def __init__(self, hashmap_size):
        self.item = []
        self.num_of_buckets = hashmap_size
        self.num_of_items = 0
        for i in range(self.num_of_buckets):
            self.item.append([])

            
    def get_num_of_buckets(self):
        return self.num_of_buckets
    
    def get_num_of_items(self):
        return self.num_of_items
    
    def get_item(self):
        return self.item
    
    def increase_num_of_items(self):
        self.num_of_items += 1
    
    
    def insert(self, new_item):
        if ( (self.get_num_of_items() / self.get_num_of_buckets()) > 1 ):
            new_hashmap = self.insert_full_hashmap(new_item)
            self.__dict__ = new_hashmap.__dict__
        else:
            index = self.get_index(new_item)
            self.item[index].append(new_item)
            self.increase_num_of_items()
            
            
    def insert_full_hashmap(self, new_item):
        new_hashmap_size = (self.get_num_of_buckets() * 2) + 1
        h = HashMap(new_hashmap_size)
        for i in range(self.get_num_of_buckets() ):
            for j in range( len(self.item[i]) ):
                h.insert( self.item[i][j] )
        h.insert(new_item)
        return h
        
    
    def get_index(self, new_item):
        c = 0
        for i in new_item:
            c += ord(i)
        return c % self.get_num_of_buckets()
    
    
    def display(self):
        for i in range( self.get_num_of_buckets() ):
            print(i, end=': ')
            for j in range( len(self.item[i]) ):
                print(self.item[i][j], end=' ')
            print()
        

if __name__ == '__main__':
    print('start program\n')
    hm = HashMap(26)
    hm.insert('nanoo')
    hm.insert('pizza')
    hm.insert('soccerr')
    
    hm.insert('bball')
    hm.display()
    
            

