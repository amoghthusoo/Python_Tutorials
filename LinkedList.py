class ListNode:

    def __init__(self, val=0, next=None):
        self.val = None
        self.next = None

class LinkedList:

    
    def insertAtStart(self, head, value):
  
        temp = ListNode()
        temp.value = value
        temp.next = head
        head = temp
        
        return head
    
    def insertAtEnd(self, head, value):
        
        temp = ListNode()
        temp.value = value
        temp.next = None

        if(head == None):
            head = temp
        else:
            traversePtr = head
            
            while(traversePtr.next != None):
                traversePtr = traversePtr.next

            traversePtr.next = temp
        
        return head
    
    def linkedListToList(self, head):

        outList = []

        traversePtr = head
        while(traversePtr != None):
            
            outList.append(traversePtr.value)
            traversePtr = traversePtr.next
        
        return outList
    
    def listToLinkedList(self, inList):
        
        outHead = None

        for element in inList:
            outHead = self.insertAtEnd(outHead, element)

        return outHead
            
    
    def showLinkedList(self, head):

        while(head != None):
            print(f"{head.value} -> ", end="")
            head = head.next

        print(None)

obj = LinkedList()
head = None
# head = obj.insertAtStart(head, 5)
# head = obj.insertAtStart(head, 15)

# head = obj.insertAtEnd(head, 5)
# head = obj.insertAtEnd(head, 6)
# head = obj.insertAtEnd(head, 7)

# outList = obj.linkedListToList(head)
# print(outList)

head = obj.listToLinkedList([1, 2, 3])
obj.showLinkedList(head)

print()
