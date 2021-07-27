# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 23:33:46 2021

@author: joaqu
"""
#using the hashmap by python aka dictionary

if __name__ == "__main__":
    print('start program\n')
    d1 = dict()
    d1.update({'giannis':47})
    d1['lopez'] = 17
    
    print(d1)
    
    
    d2 = dict( {'nash':32, 'booker':25, 'paul':30, 'lonzo':4, 'melo':6, 'rocks':0})
    del d2['lonzo']
    d2.pop('melo')
    d2['rocks'] = 1
    
    for i in d2:
        print(i)
    print('.')
        
    for k in d2.keys():
        print(k)
    print('.')
    
    for j in d2.values():
        print(j)
    print('.')
        
    for m in d2.items():
        print(m)
        
    for key,item in d2.items():
        print(key, '+', item)
    print('.')
    
    #adds the d1 dict to the d2 dict
    # d2.update(d1)
    
    print(d2.get('paul'))
    print(d2)
    
    
    k1 = ['jack', 'nico', 'tony']
    v1 = [26, 2, 37]
    
    d5 = {k:v for k,v in zip(k1,v1) }
    print(d5)
    
    o1 = {'soccer':100, 'bball':90, 'golf':30, 'ufc':80}
    d7 = dict()
    d7.update(o1)
    d7.pop('golf')
    print(d7)
    
    
    
    