class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
        self.previous=None

class DoublyLinkedList:
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
            newNode.previous=self.tail
            self.tail=newNode
        self.size+=1
        return self
    def show(self,reverse=0):
        if reverse==0:
            if self.size==0:
                print("List is Empty")
            else:
                print("LinkedList Items: ",end="")
                tempNode=self.head
                while tempNode!=None:
                    print(tempNode.value,end=" ")
                    tempNode=tempNode.next
            print()
        else:
            if self.size==0:
                print("List is Empty")
            else:
                print("LinkedList Items: ",end="")
                tempNode=self.tail
                while tempNode!=None:
                    print(tempNode.value,end=" ")
                    tempNode=tempNode.previous
            print()

    def prepend(self,value):
        newNode=Node(value)
        if self.size==0:
            self.tail=newNode
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.previous=newNode
            self.head=newNode
        self.size+=1
        return self        

    def popLast(self):
        if self.size==0:
            raise Exception("List is Empty")
        poppedNode=self.tail
        if self.size==1:
            self.head=None
            self.tail=None
            self.size=0
            return poppedNode.value
        self.tail=self.tail.previous
        self.tail.next=None
        poppedNode.previous=None
        self.size-=1
        return poppedNode.value

    def removeNodeByValue(self,value):
        if self.size==0:
            raise Exception("List is Empty")
        if value==self.head.value:
            return self.popFirst()
        if value==self.tail.value:
            return self.popLast()
        tempNode=self.head
        while tempNode.next.value != value:
            tempNode=tempNode.next
        removedNode=tempNode.next
        tempNode.next=removedNode.next
        nextNode=removedNode.next
        nextNode.previous=tempNode
        removedNode.next=None
        removedNode.previous=None
        self.size-=1
        return removedNode.value