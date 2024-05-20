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
    

t=BinarySearchTree()
t.insert(25)
t.insert(22)
t.insert(27)
t.insert(40)
t.insert(43)
t.insert(65)
t.insert(400)
t.insert(-43)
x=t.bft()
print(x)
res=t.search(220)
print(res)