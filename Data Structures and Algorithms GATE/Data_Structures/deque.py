from doubly_linked_list import DoublyLinkedList

class Deque:

    def __init__(self):
        self.deque = DoublyLinkedList()

    def append(self, val):
        self.deque.insert_at_end(val)

    def append_left(self, val):
        self.deque.insert_at_start(val)

    def pop(self):
        
        if(not self.is_empty()):
            return self.deque.delete_from_end()
        else:
            return None

    def pop_left(self):
        
        if(not self.is_empty()):
            return self.deque.delete_from_start()
        else:
            return None

    def front(self):
        
        if(not self.is_empty()):
            return self.deque.head.val
        else:
            return None

    def rear(self):
        
        if(not self.is_empty()):
            return self.deque.rear.val
        else:
            return None

    def is_empty(self):
        
        if(self.deque.length == 0):
            return True
        else:
            return False

def main():
    
    dq = Deque()

    dq.append(5)
    dq.append(6)
    dq.append(7)

    dq.append_left(100)
    dq.append_left(200)
    dq.append_left(300)

    print(dq.front())
    print(dq.rear())

    print(dq.pop())
    print(dq.pop_left())
    


if(__name__ == "__main__"):
    main()
