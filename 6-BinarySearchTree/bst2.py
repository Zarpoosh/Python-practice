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

                           