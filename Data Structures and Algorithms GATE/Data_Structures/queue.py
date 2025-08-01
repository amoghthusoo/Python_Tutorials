from linked_list import LinkedList

class Queue:

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, val):
        self.queue.insert_at_end(val)

    def dequeue(self):
        
        if(not self.is_empty()):
            return self.queue.delete_from_start()
        else:
            return None

    def front(self):
        
        if(not self.is_empty()):
            return self.queue.head.val
        else:
            return None

    def rear(self):
        
        if(not self.is_empty()):
            return self.queue.rear.val
        else:
            return None

    def is_empty(self):
        
        if(self.queue.length == 0):
            return True
        else:
            return False

def main():
    
    q = Queue()

    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)

    print(q.front())
    print(q.rear())


if(__name__ == "__main__"):
    main()

