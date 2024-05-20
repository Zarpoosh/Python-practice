class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
        
    def insert(self,value):
        newNode=Node(value)
        if self.root == None:
            self.root=newNode
            return self
        tempNode=self.root
        while value != tempNode.value:
            # print(tempNode.value)
            if value<tempNode.value:
                if tempNode.left==None:
                    tempNode.left=newNode
                    break
                tempNode=tempNode.left
            else:
                if tempNode.right==None:
                    tempNode.right=newNode
                    break
                tempNode=tempNode.right
        return self 

    def bft(self):
        if self.root == None:
            print("Tree is Empty")
            return
        queue=list()
        queue.append(self.root)
        visited=list()
        while queue:
            visitedNode=queue.pop(0)
            visited.append(visitedNode.value)
            if visitedNode.left !=None:
                queue.append(visitedNode.left)
            if visitedNode.right !=None:
                queue.append(visitedNode.right)
        return visited
    
    def search(self,value):
        tempNode=self.root
        while tempNode != None:
            if value==tempNode.value:
                return True
            if value < tempNode.value:
                tempNode=tempNode.left
            else:
                tempNode=tempNode.right
        return False
    
    def dftPreOrder(self):
        if self.root == None:
            print("Tree is Empty")
            return
        stack=list()
        stack.append(self.root)
        visited=list()
        while stack:
            visitedNode=stack.pop()
            visited.append(visitedNode.value)
            if visitedNode.right !=None:
                stack.append(visitedNode.right)
            if visitedNode.left !=None:
                stack.append(visitedNode.left)
        return visited
    
    def dftInOrder(self):
        if self.root == None:
            print("Tree is Empty")
            return
        tempNode=self.root
        stack=list()
        visited=list()
        visitedValue=list()
        while stack or tempNode !=None:
            if tempNode != None:
                stack.append(tempNode)
                tempNode=tempNode.left
            else:
                visitedNode=stack.pop()
                visited.append(visitedNode)
                visitedValue.append(visitedNode.value)
                if visitedNode.right ==None:
                    continue
                tempNode=visitedNode.right
        return visitedValue

    def dftPostOrder(self):
        if self.root == None:
            print("Tree is Empty")
            return
        currentNode=self.root
        previousNode=self.root
        stack=list()
        visited=list()
        while currentNode != None:
            while currentNode.left != None:
                stack.append(currentNode)
                currentNode=currentNode.left
            while currentNode.right==None or currentNode.right==previousNode:
                visited.append(currentNode.value)
                previousNode=currentNode
                if not stack:
                    return visited
                currentNode=stack.pop()
            stack.append(currentNode)
            currentNode=currentNode.right




t=BinarySearchTree()
t.insert(25)
t.insert(22)
t.insert(27)
t.insert(40)
t.insert(43)
t.insert(65)
t.insert(400)
t.insert(-43)
t.insert(38)
t.insert(55)
t.insert(39)
x=t.bft()
print(x)
res=t.search(220)
print(res)
x=t.dftPreOrder()
print(x)
x=t.dftInOrder()
print(x)
x=t.dftPostOrder()
print(x)