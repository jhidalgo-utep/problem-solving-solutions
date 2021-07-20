# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 13:43:12 2021

@author: joaqu
"""

class HashMap(object):
    def __init__(self, hash_size):
        self.item = []
        self.num_of_buckets = hash_size
        self.num_of_items = 0
        for i in range(hash_size):
            self.item.append([])
    
    def get_num_of_buckets(self):
        return self.num_of_buckets
    
    def get_num_of_items(self):
        return self.num_of_items
    
    def insert(self, new_item):
        if ( self.get_num_of_items() / self.get_num_of_buckets() ) > 1:
            new_hashmap = self.full_insert(new_item)
            self.__dict__ = new_hashmap.__dict__
            
        else:
            index = self.hash_func(new_item)
            self.item[index].append(new_item)
            self.num_of_items += 1
    
    
    def full_insert(self, new_item):
        new_hashmap_size = (self.get_num_of_buckets() * 2) + 1
        H = HashMap(new_hashmap_size)
        
        for i in range(len(self.item)):
            for j in range(len(self.item[i]) ):
                H.insert( self.item[i][j] )
                
        H.insert(new_item)
        return H
        
    
    def hash_func(self, word):
        r = 0
        for c in word:
            r += ord(c)
        return r % self.get_num_of_buckets()
    
    def print_hashmap(self):
        for i in range(len(self.item)):
            print(i, end = ': ')
            for j in range(len(self.item[i]) ):
                print(self.item[i][j], end = ' ')
            print()
            
            

if __name__ == "__main__":
    print('start program')
    
    hm = HashMap(2)
    
    hm.insert('soccer')
    hm.insert('nano')
    hm.insert('bball')
    hm.insert('pizza')
    hm.insert('kitty')
    hm.print_hashmap()
    
    