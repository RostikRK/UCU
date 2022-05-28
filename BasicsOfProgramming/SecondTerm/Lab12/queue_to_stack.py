"""
Queue to stack converter.
"""

from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    """
    Makes stack from queue
    """
    stack = ArrayStack()
    liist = []
    for elem in queue:
        liist.append(elem)
    liist.reverse()
    for elem in liist:
        stack.add(elem)
    return stack
