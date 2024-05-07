class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.size=0
    
    def append(self,value):
        newNode=Node(value)
        if self.size==0:
            self.tail=newNode
            self.head=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.size+=1
        return self
    
    def show(self):
        if self.size==0:
            print("List is Empty")
        else:
            print("LinkedList Items: ",end="")
            tempNode=self.head
            while tempNode!=None:
                print(tempNode.value,end=" ")
                tempNode=tempNode.next
            print()

    def prepend(self,value):
        newNode=Node(value)
        if self.size==0:
            self.tail=newNode
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.size+=1
        return self        

    def getIndexByValue(self,value): # search
        index=0
        if self.size==0:
            return -1 # Not Found
        tempNode=self.head
        while tempNode!=None:
            if tempNode.value==value:
                return index
            tempNode=tempNode.next
            index+=1
        return -1
    
    def getValueByIndex(self,index):
        if index>=self.size or index<0:
            raise IndexError(f"LinkedList Index Out of Range (0<=index<={self.size-1})")
        tempNode=self.head
        for i in range(index):
            tempNode=tempNode.next
        return tempNode.value
    
    def popLast(self):
        if self.size==0:
            raise Exception("List is Empty")
        poppedNode=self.tail
        if self.size==1:
            self.head=None
            self.tail=None
            self.size=0
            return poppedNode.value
        tempNode=self.head
        while tempNode.next !=self.tail:
            tempNode=tempNode.next
        self.tail=tempNode
        self.tail.next=None
        self.size-=1
        return poppedNode.value
    
    def popFirst(self):
        if self.size==0:
            raise Exception("List is Empty")
        poppedNode=self.head
        if self.size==1:
            self.head=None
            self.tail=None
            self.size=0
            return poppedNode.value
        self.head=self.head.next
        poppedNode.next=None
        self.size-=1
        return poppedNode.value
    

s=SinglyLinkedList()
s.append(5)
s.append(23)
s.append(78)
s.prepend(45)
s.prepend(77)
s.append(90)
s.append(22)    
s.show()
value=s.popFirst()
print(value)
s.show()
value=s.popFirst()
print(value)
s.show()