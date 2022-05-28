"""
Class Node
"""
class Node:

    def __init__(self, item, next=None):
        """Instantiates a Node with default next of None"""
        self.item = item
        self.next = next
