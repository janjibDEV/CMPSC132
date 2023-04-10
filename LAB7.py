# LAB7
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

class MaxBinaryHeap:
    '''
        >>> h = MaxBinaryHeap()
        >>> h.getMax
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [10, 5]
        >>> h.insert(14)
        >>> h._heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(14)
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> h.insert(20)
        >>> h
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.insert(20)
        >>> h
        [20, 20, 14, 14, 2, 10, 11, 5, 9]
        >>> h.getMax
        20
        >>> h._leftChild(1)
        20
        >>> h._rightChild(1)
        14
        >>> h._parent(1)
        >>> h._parent(6)
        14
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMax()
        20
        >>> h._heap
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.deleteMax()
        20
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> len(h)
        7
        >>> h.getMax
        14
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMax(self):
        # YOUR CODE STARTS HERE
        pass
    
    def _parent(self,index):
        # YOUR CODE STARTS HERE
        pass
        

    def _leftChild(self,index):
        # YOUR CODE STARTS HERE
        pass


    def _rightChild(self,index):
        # YOUR CODE STARTS HERE
        pass
         

    def insert(self,x):
        # YOUR CODE STARTS HERE
        pass

    def deleteMax(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            removed=self._heap[0]
            self._heap=[]
            return removed 

        # YOUR CODE STARTS HERE
        pass


def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [8, 5, 4, 3.1, 2, 1, 0, -15, -15, -15]
    '''
    # YOUR CODE STARTS HERE
    pass



# ============== EXTRA CREDIT
class PriorityQueue:
    '''
        >>> priority_q = PriorityQueue()
        >>> priority_q.isEmpty()
        True
        >>> priority_q.peek()
        >>> priority_q.enqueue('sara',0)
        >>> priority_q
        [(0, 'sara')]
        >>> priority_q.enqueue('kyle',3)
        >>> priority_q
        [(3, 'kyle'), (0, 'sara')]
        >>> priority_q.enqueue('harsh',1)
        >>> priority_q
        [(3, 'kyle'), (0, 'sara'), (1, 'harsh')]
        >>> priority_q.enqueue('ajay',5)
        >>> priority_q
        [(5, 'ajay'), (3, 'kyle'), (1, 'harsh'), (0, 'sara')]
        >>> priority_q.enqueue('daniel',4)
        >>> priority_q.isEmpty()
        False
        >>> priority_q
        [(5, 'ajay'), (4, 'daniel'), (1, 'harsh'), (0, 'sara'), (3, 'kyle')]
        >>> priority_q.enqueue('ryan',7)
        >>> priority_q
        [(7, 'ryan'), (4, 'daniel'), (5, 'ajay'), (0, 'sara'), (3, 'kyle'), (1, 'harsh')]
        >>> priority_q.dequeue()
        'ryan'
        >>> priority_q.peek()
        'ajay'
        >>> priority_q
        [(5, 'ajay'), (4, 'daniel'), (1, 'harsh'), (0, 'sara'), (3, 'kyle')]
        >>> priority_q.dequeue()
        'ajay'
        >>> len(priority_q)
        4
        >>> priority_q.dequeue()
        'daniel'
        >>> priority_q.dequeue()
        'kyle'
        >>> priority_q.dequeue()
        'harsh'
        >>> priority_q.dequeue()
        'sara'
        >>> priority_q.dequeue()
        >>> priority_q.isEmpty()
        True
    '''

    def __init__(self):
        self._items = MaxBinaryHeap()

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    __repr__ = __str__

    def peek(self):
        # YOUR CODE STARTS HERE
        pass

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        pass
    
    def enqueue(self, value, priority):
        # YOUR CODE STARTS HERE
        pass
    
    def dequeue(self):
        # YOUR CODE STARTS HERE
        pass
    




