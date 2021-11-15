# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:54:51 2021

@author: joaqu
"""

class HashMap(object):
    def __init__(self, size):
        self.item = []
        self.num_buckets = size
        self.num_items = 0
        for i in range(size):
            self.item.append( [] )
    
    def display(self):
        for i in range(len(self.item)):
            for j in range(len(self.item[i]) ):
                print(self.item[i][j], end = ' ')
            print('\n')
    
    def insert(self, new_item):
        if (self.num_items / self.num_buckets) > 1:
            new_hash = self.insert_full(new_item)
            self.__dict__ = new_hash.__dict__
            
        else:
            index = get_hash(new_item)
            self.item[index].append(new_item)
            self.num_items += 1
            
    
    def insert_full(self, new_item):
        new_size = self.num_buckets
        h = HashMap(new_size)
        
        for i in range(len(self.item)):
            for j in range(len(self.item[i]) ):
                h.insert(self.item[i][j])
        
        h.insert(new_item)
        return h
        
    
    def get_hash(self, word):
        res = 0
        for c in word:
            res += ord(c)
        return res % self.num_buckets
    
    
if __name__ == "__main__":
    print('start\n')
    
    d = dict()
    d['soccer'] = 10
    d['movie'] = 2
    # d.pop('soccer')
    del d['soccer']
    d.update( {'baseball':20})
    print(d)
    
    
    name = ['a', 'b', 'c', 'd']
    age = [1,2,3,4]
    
    d2 = dict()
    
    d2 = {k:v for k,v in zip(name, age)}
    print(d2)
    
        
        
        
        
        
        
        