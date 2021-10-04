# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:45:14 2021

@author: joaqu
"""
# mins

class HashMap(object):
    def __init__(self, size):
        self.item = []
        self.num_of_buckets = size
        self.num_of_items = 0
        for i in range(size):
            self.item.append([])
    
    def insert(self, new_item):
        if self.num_of_items / self.num_of_buckets > 1:
            print('here')
            new_hash = self.insert_full(new_item)
            self.__dict__ = new_hash.__dict__
            
        else:
            index = self.get_hash(new_item)
            self.item[index].append(new_item)
            self.num_of_items += 1
    
    def insert_full(self, new_item):
        new_size = self.num_of_buckets * 2 + 1
        h = HashMap(new_size)
        for i in range(len(self.item) ):
            for j in range(len(self.item[i]) ):
                h.insert(self.item[i][j])
        h.insert(new_item)
        return h
    
    def get_hash(self, word):
        result = 0
        for c in word:
            result += ord(c)
        return result % self.num_of_buckets
        
    
    def display(self):
        for i in range(len(self.item) ):
            for j in range(len(self.item[i]) ):
                print(self.item[i][j], end = ' ')
            print()


if __name__ == "__main__":
    print('start\n')
    h = HashMap(2)
    h.insert('pie')
    h.insert('alogra')
    h.insert('tre')
    # h.insert('now')
    h.display()
    
    
    h2 = dict()
    h2['joe'] = 20
    h2['solo'] = 18
    h2['point'] = 12
    h2.update( {'secrect':7, 'hours':24} )
    h2.pop('solo')
    print(h2)
    h2['time'] = 100
    print(h2)
    del h2['time']
    print(h2)
    
    
    for k,v in h2.items():
        print( k, v)
        
    name = ['a', 'b', 'c']
    age = [10, 20, 30]
    
    h3 = {k:v for k,v in zip(name, age) }
    print(h3)