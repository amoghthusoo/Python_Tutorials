class ListNode:

    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    def insert_at_start(self, val):

        temp = ListNode(val)

        if(self.head is None):
            self.head = self.rear = temp
        
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        
        self.length += 1

    def insert_at_end(self, val):

        temp = ListNode(val)

        if(self.head is None):
            self.head = self.rear = temp

        else:
            temp.prev = self.rear
            self.rear.next = temp
            self.rear = temp
        
        self.length += 1

    def delete_from_start(self):

        if(self.head is None):
            return None
        
        elif(self.head.next is None):

            deleted_val = self.head.val
            self.head = self.rear = None
        
        else:

            deleted_val = self.head.val
            self.head = self.head.next
            self.head.prev = None
        
        self.length -= 1
        return deleted_val
    

    def delete_from_end(self):

        if(self.head is None):
            return None
        
        elif(self.head.next is None):
            deleted_val = self.head.val
            self.head = self.rear = None
        
        else:
            deleted_val = self.rear.val
            self.rear = self.rear.prev
            self.rear.next = None
        
        self.length -= 1
        return deleted_val
    
    def display(self):

        ptr = self.head
        while(ptr):
            print(ptr.val, end = "")

            if(ptr.next is not None):
                print(" -> ", end = "")
            
            ptr = ptr.next

        print()

        ptr = self.rear
        while(ptr):
            print(ptr.val, end = "")

            if(ptr.prev is not None):
                print(" -> ", end = "")
            
            ptr = ptr.prev

def main():

    l1 = DoublyLinkedList()
    l1.insert_at_start(7)
    l1.insert_at_start(6)
    l1.insert_at_start(5)

    l1.delete_from_start()
    l1.delete_from_start()

    l1.insert_at_end(5)
    l1.insert_at_end(6)
    l1.insert_at_end(7)

    l1.delete_from_end()
    l1.delete_from_end()

    l1.display()

if(__name__ == "__main__"):
    main()
