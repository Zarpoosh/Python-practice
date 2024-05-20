from DoublyLinkedList import DoublyLinkedList as DLL

myList=DLL()
myList.append(27)
myList.prepend(83)
myList.append(22)
myList.show()
x=myList.popLast()
print(x)
myList.show()