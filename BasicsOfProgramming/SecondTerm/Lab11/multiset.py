"""Multiset"""
import node
class Multiset:
    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        init: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None
    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None
    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        contains: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False
    def add(self, value):
        """
        Adds the value to multiset.
        :param value: the value to be added.
        """
        if self._head is None:
            self._head = node.Node(value)
        else:
            rest = self._head
            self._head = node.Node(value)
            self._head.next = rest
    def delete(self, value):
        """
        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next
    def remove_all(self):
        """
        приймає один аргумент - посилання на однозв’язаний список, по черзі \n
        видаляє всі його вузли та повертає всі значення у list
        """
        elements = []
        current = self._head
        while current is not None:
            elements.append(current.item)
            current = current.next
        self._head = None
        return elements
    def split_half(self):
        """
        приймає посилання на однозв’язаний список, ділить її на 2
        """
        multiset_1 = Multiset()
        multiset_2 = Multiset()
        half1 = (self.__len__() + 1) // 2
        half2 = self.__len__() // 2
        current = self._head
        if len(self) != 1:
            while half1 > 0:
                half1 -= 1
                multiset_1.add_in_the_end(current.item)
                current = current.next
            while half2 > 0:
                half2 -= 1
                multiset_2.add_in_the_end(current.item)
                current = current.next
            return multiset_1, multiset_2
        else:
            return None
    def extend(self, other):
        """
        приймає посилання на два однозв'язані списки та
        """
        multiset = Multiset()
        current1 = other._head
        while current1 is not None:
            multiset.add_in_the_end(current1.item)
            current1 = current1.next
        current2 = self._head
        while current2 is not None:
            multiset.add_in_the_end(current2.item)
            current2 = current2.next
        return multiset
    def add_in_the_end(self, value):
        """
        Add in the end
        """
        if self._head is None:
            self._head = node.Node(value)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = node.Node(value)
    def __len__(self):
        length = 0
        current = self._head
        while current is not None:
            length += 1
            current = current.next
        return length
    def __str__(self):
        elements = []
        cur = self._head
        while cur is not None:
            elements.append(cur.item)
            cur = cur.next
        return str(elements)
