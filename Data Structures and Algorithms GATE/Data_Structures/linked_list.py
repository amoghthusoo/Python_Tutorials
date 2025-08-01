class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    def insert_at_start(self, val):

        temp = ListNode(val)

        if(self.head  is None):
            self.head = self.rear = temp
        
        else:
            temp.next = self.head
            self.head = temp

        self.length += 1
    
    def insert_at_end(self, val):

        temp = ListNode(val)

        if(self.head is None):
            self.head = self.rear = temp

        else:
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

        self.length -= 1
        return deleted_val

    def delete_from_end(self):

        if(self.head is None):
            return None
        
        elif(self.head.next is None):
            deleted_val = self.head.val
            self.head = self.rear = None

        else:
            ptr = self.head

            while(ptr.next.next is not None):
                ptr = ptr.next

            deleted_val = ptr.next.val    
            ptr.next = None
            self.rear = ptr

            self.length -= 1
            return deleted_val

    def display(self):

        ptr = self.head
        while(ptr):
            print(ptr.val, end = "")

            if(ptr.next != None):
                print(" -> ", end = "")
            
            ptr = ptr.next

def main():

    l1 = LinkedList()
    l1.insert_at_end(5)
    l1.insert_at_end(6)
    l1.insert_at_end(7)

    print(l1.length)

    # print(l1.delete_from_end())
    # print(l1.delete_from_start())

    l1.insert_at_end(8)

    l1.display()

if(__name__ == "__main__"):
    main()
