"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

import sys
sys.path.append('../stack')
sys.path.append('../queue')
from stack import *
from queue import *

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if not self.value:
        #     self.value = value:
        #     return True
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(vaule)
            
        elif value >= self.value:
            if self.right in None:
                self.right = BSTNode(value)
            else self.right.insert(value)

        


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if this is the target you found it
        if target == self.value:
            return "self.node"
        #if target < this go left and look again
        elif target < self.value:
            self.value = self.left
            self.contains
        #if not left do it to the right
        else:
            self.value = self.right
            self.contains


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #lowest num is furthest left.
        #a = []
        
        if node is None: 
            return
        self.in_order_print(self.left)
        print(node.value)
        self.in_order_print(self.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            popped = queue.dequeue()
            print(popped.value)
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            popped = stack.pop()
            print(popped.value)
            if popped.left:
                stack.push(popped.left)
            if popped.right:
                stack.push(popped.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
