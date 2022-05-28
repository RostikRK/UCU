"""
File: linkedbst.py
Author: Ken Lambert
"""
from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
from math import log2, ceil


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it'strun present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            strun = ""
            if node != None:
                strun += recurse(node.right, level + 1)
                strun += "| " * level
                strun += str(node.data) + "\n"
                strun += recurse(node.left, level + 1)
            return strun

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right != None:
                    stack.push(node.right)
                if node.left != None:
                    stack.push(node.left)

    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        return None

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        return None

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        return None

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item'strun position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
                # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item'strun spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftmaxinleftsubtreetotop(top):
            # Replace top'strun datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top'strun left subtree
            #       has been removed
            # Post: top.data = maximum value in top'strun left subtree
            parent = top
            curretnode = top.left
            while not curretnode.right == None:
                parent = curretnode
                curretnode = curretnode.right
            top.data = curretnode.data
            if parent == top:
                top.left = curretnode.left
            else:
                parent.right = curretnode.left

        # Begin main part of the method
        if self.isEmpty():
            return None

        # Attempt to locate the node containing the item
        itemrem = None
        preroot = BSTNode(None)
        preroot.left = self._root
        parent = preroot
        direction = 'L'
        curretnode = self._root
        while not curretnode == None:
            if curretnode.data == item:
                itemrem = curretnode.data
                break
            parent = curretnode
            if curretnode.data > item:
                direction = 'L'
                curretnode = curretnode.left
            else:
                direction = 'R'
                curretnode = curretnode.right

        # Return None if the item is absent
        if itemrem == None:
            return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node'strun value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not curretnode.left == None \
                and not curretnode.right == None:
            liftmaxinleftsubtreetotop(curretnode)
        else:

            # Case 2: The node has no left child
            if curretnode.left == None:
                newchi = curretnode.right

                # Case 3: The node has no right child
            else:
                newchi = curretnode.left

                # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newchi
            else:
                parent.right = newchi

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection'strun size counter
        #            Return the item
        self._size -= 1
        if self.isEmpty():
            self._root = None
        else:
            self._root = preroot.left
        return itemrem

    def replace(self, item, newite):
        """
        If item is in self, replaces it with newite and
        returns the old item, or returns None otherwise."""
        probe = self._root
        while probe != None:
            if probe.data == item:
                olddat = probe.data
                probe.data = newite
                return olddat
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self, nod = None):
        '''
        Return the height of tree
        :return: int
        '''
        def height1(top):
            '''
            Helper function
            :param top:
            :return:
            '''
            if top.left == None and top.right == None:
                return 0
            else:
                return 1 + max(height1(nood) for nood in (top.left, top.right) if nood != None)
        if nod is None:
            nod = self._root
        return height1(nod)

    def is_balanced(self):
        '''
        Return True if tree is balanced
        :return:
        '''
        if self.height() < (2 * log2(self._size + 1) - 1):
            return True
        else:
            return False

    def range_find(self, low, high):
        '''
        Returns a list of the items in the tree, where low <= item <= high."""
        :param low:
        :param high:
        :return:
        '''
        lyst = list()

        def recurse(node):
            if node != None:
                if (low <= node.data <= high):
                    recurse(node.left)
                    lyst.append(node.data)
                    recurse(node.right)
                elif node.data <= low:
                    recurse(node.right)
                elif node.data >= high:
                    recurse(node.left)
        recurse(self._root)
        return lyst

    def rebalance(self):
        '''
        Rebalances the tree.
        :return:
        '''
        iteral = self.inorder()

        def rebl1(iteral):
            if len(iteral) == 0:
                return None
            i = len(iteral) // 2
            node = BSTNode(iteral[i])
            node.left = rebl1(iteral[:i])
            node.right = rebl1(iteral[i+1:])
            return node
        self._root = rebl1(list(iteral))

    def successor(self, item, probe=None, root=None, count=0):
        """
        Returns the smallest item that is larger than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        def findmin(root):
            while root.left != None:
                root = root.left
            return root
        if self._root is None:
            return probe
        elif root == None and count == 0:
            root = self._root
            count += 1
        elif root == None and count != 0:
            probe = None
            return probe
        if item == root.data:
            if root.right:
                probe = findmin(root.right)
        if item < root.data:
            # if root.left.data > item:
            # else:
            # if root.right:
            probe = findmin(root)
            if root.left != None:
                return self.successor(item, probe, root.left, count)
        else:
            return self.successor(item, probe, root.right, count)
        return probe.data

    def predecessor(self, item):
        """
        Returns the largest item that is smaller than
        item, or None if there is no such item.
        :param item:
        :type item:
        :return:
        :rtype:
        """
        nodes = sorted(list(self.inorder()))
        for i in range(len(nodes)-1, -1, -1):
            if item > nodes[i]:
                return nodes[i]
