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


dl=DoublyLinkedList()
dl.append(24)
dl.append(0)
dl.append(90)
dl.append(26)
dl.show()
dl.show(reverse=1)
