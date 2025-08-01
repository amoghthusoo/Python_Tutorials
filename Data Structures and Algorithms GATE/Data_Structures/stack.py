from linked_list import LinkedList

class Stack:

    def __init__(self):
        self.stack = LinkedList()

    def push(self, val):
        
        self.stack.insert_at_start(val)

    def pop(self):
        
        if(not self.is_empty()):
            return self.stack.delete_from_start()
        else:
            return None

    def top(self):

        if(not self.is_empty()):
            return self.stack.head.val
        else:
            return None

    def is_empty(self):
        
        if(self.stack.length == 0):
            return True
        else:
            return False

def main():
    
    s = Stack()

    s.push(3)
    s.push(4)
    s.push(5)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())


if(__name__ == "__main__"):
    main()