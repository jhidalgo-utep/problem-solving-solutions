# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:13:05 2021

@author: joaqu
"""

class HashMap(object):
    def __init__(self, size):
        self.item = []
        self.num_of_items = 0
        self.num_of_buckets = size
        for i in range(size):
            self.item.append( [] )
    
    def display(self):
        print(self.item)
    
    def insert(self, new_item):
        if (self.num_of_items / self.num_of_buckets) > 1:
            new_hash = self.insert_full(new_item)
            self.__dict__ = new_hash.__dict__
        else:
            index = self.get_hash(new_item)
            self.item[index].append(new_item)
            self.num_of_items += 1
            
    def insert_full(self, new_item):
        new_size = (self.num_of_buckets * 2) + 1
        h = HashMap(new_size)
        for i in range(self.item):
            for j in range(self.item[i] ):
                h.insert(self.item[i][j] )
        h.insert(new_item)
        return h
            
    
    def get_hash(self, word):
        res = 0
        for c in word:
            res += ord(c)
        return res % self.num_of_buckets
    
    
if __name__ == "__main__":
    print('start\n')
    
    h = dict()
    
    h.update({'soccer':11})
    h['pencil'] = 4
    h.pop('pencil')
    h['house music'] = 20
    
    print(h)
    
    name = ['a', 'b', 'c', 'd']
    age = [1,2,3,4]
    
    h2 = {k:v for k,v in zip(name,age)}
    print(h2)
        
        
        
        
        
        
        
        