# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:00:42 2021

@author: joaqu
"""
from HashMap import HashMap

if __name__ == "__main__":
    print('start program\n')
    
    # ### Custom HashMap.py
    # h = HashMap(2)
    # h.insert('soccer')
    # h.insert('basketball')
    # h.insert('football')
    # h.insert('pizza')
    # h.display()
    
    
    ### method 1
    hm = dict()
    
    #insert
    hm.update({'soccer':3})
    hm['basketball'] = 7
    hm['kitty'] = 10
    hm['hockey'] = 2
    hm.update({'polo': 8})
    
    #remove
    hm.pop('soccer')
    del hm['hockey']
    
    #increase value
    hm['kitty'] = hm.get('kitty') + 1
    hm['kitty'] += 1
    
    # for k in hm.keys():
    #     print(k)
        
    # for v in hm.values():
    #     print(v)
        
    # for k,v in hm.items():
    #     print(v)
    
    
    #### method 2
    h10 = {'rocky':1, 'asap':2, 'check':3}
    print(h10)
    
    
    ### method 3
    name = ["jack", "kitty", "nano"]
    age = [26, 60, 50]
    
    h5 = {k:v for k,v in zip(name, age)}
    print(h5)
    
    
    
    