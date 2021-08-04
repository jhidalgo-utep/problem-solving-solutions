# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:26:30 2021

@author: joaqu
"""

from Trie import Trie

if __name__ == "__main__":
    print('start program\n')
    
    t = Trie()
    t.insert('soccer')
    t.insert('socks')
    print( t.search_prefix('socks') )