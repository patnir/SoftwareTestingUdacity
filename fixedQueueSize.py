# -*- coding: utf-8 -*-
"""
Created on Sun May 29 20:44:16 2016

@author: Rahul Patni
"""

import array
import random

class Queue:
    def __init__(self, size_max):
        assert size_max > 0
        self.max = size_max
        #initialize head and tail pointers        
        self.head = 0 
        self.tail = 0
        self.size = 0
        # researving space for queue elements
        # not using list because they natively 
        # support enqueue and dequeue operations
        # Dynamic allocation of lists make them slow
        # Only store integers to make the queue faster
        # Static queue:        
        self.data = array.array('i', range(size_max))
        
    def empty(self):
        # return true if the size if zero
        return self.size == 0
        
    def full(self):
        # return true if the size if equal the max size
        return self.size == self.max
        
    def enqueue(self, x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        #if tail moves past the queue, reset tail
        if self.tail == self.max:
            self.tail = 0
        return True
        
    def dequeue(self):
        if self.size == 0:
            return None
        #return number pointed to by head
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x
        
def usingQueue():
    q = Queue(2)
    print q.empty() #True
    print q.full() #False
    print q.enqueue(6) #True
    print q.enqueue(7) #True
    print q.full() #True
    print q.enqueue(8) #False
    print q.full() #True
    print q.dequeue() #6
    print q.dequeue() #7
    print q.dequeue() #None
    print q.empty() #True
    
usingQueue()
    