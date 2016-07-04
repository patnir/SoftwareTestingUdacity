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


def test2():
    ###Your code here.
    # Check if q is empty
    q = Queue(2)
    res = q.dequeue()
    if (res != None):
        print "test 2 NOT OK (dequeue when empty)" 
        return
    res = q.enqueue(7)
    if not res:
        print "test2 NOT OK"
        return
    res = q.enqueue(8)
    if not res:
        print "test2 NOT OK"
        return
    res = q.dequeue()
    if q.head != 1:
        print "test2 NOT OK"
        return
    res = q.dequeue()
    if q.head != 0:
        print "test2 NOT OK"
        return
    print "test2 OK"
    

def test3():
    ###Your code here.
    # Check if queue is full
    q = Queue(2)
    res = q.enqueue(7)
    if not res:
        print "test3 NOT OK"
        return
    res = q.enqueue(8)
    if not res:
        print "test3 NOT OK"
        return
    res = q.enqueue(9)
    if res:
        print "test3 NOT OK (should be full)"
        return
    if q.tail != 0 and q.size == q.max:
        print "test3 NOT OK (tail should be 0)"
    print "test3 OK"


def test1():
    q = Queue(3)
    res = q.empty()
    if not res:
        print "test1 NOT OK"
        return
    res = q.enqueue(10)
    if not res:
        print "test1 NOT OK"
        return
    res = q.enqueue(11)
    if not res:
        print "test1 NOT OK"
        return
    x = q.dequeue()
    if x != 10:
        print "test1 NOT OK"
        return
    x = q.dequeue()
    if x != 11:
        print "test1 NOT OK"
        return
    res = q.empty()
    if not res:
        print "test1 NOT OK"
        return
    print "test1 OK"

test1()
test2()
test3() 
    