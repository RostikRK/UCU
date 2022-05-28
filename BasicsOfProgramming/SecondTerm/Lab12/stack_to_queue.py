"""
Stack to queue converter.
"""


from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """
    Makes stack from queue
    """
    queue = ArrayQueue()
    liist = []
    for elem in stack:
        liist.append(elem)
    liist.reverse()
    for elem in liist:
        queue.add(elem)
    return queue
