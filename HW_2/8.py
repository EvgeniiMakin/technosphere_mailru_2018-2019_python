from collections import deque

class BinarySearchTree:
    class TreeNode:
    
        def __init__(self,val,left=None,right=None,parent=None):
            self.val = val
            self.leftChild = left
            self.rightChild = right
            self.parent = parent
        
        
        def setLeftChild(self, newleft):
            self.leftChild = newleft
            
        def setRightChild(self, newright):
            self.rightChild = newright   
        
        def hasLeftChild(self):
            return self.leftChild

        def hasRightChild(self):
            return self.rightChild

                        
        def iterLayers(self):
            q = deque()
            q.append(self)
            def layerIterator(layerSize):
                for i in range(layerSize):
                    n = q.popleft()
                    if n.leftChild: q.append(n.leftChild)
                    if n.rightChild: q.append(n.rightChild)
                    yield n.val
            while (q):
                yield from layerIterator(len(q))
       
        def __iter__(self):
            for elem in self.iterLayers():
                yield elem
                

    #the BinarySearchTree class
    
        
    def __init__(self, root=None):
        if root == None:
            self.root = None
        else:
            self.root = BinarySearchTree.TreeNode(root)

    def __iter__(self):
        if self.root == None:
            return self
        else:
            return self.root.__iter__()
    def __next__(self):
        if self.root == None:
            raise StopIteration()
    def append(self,val):
        if self.root:
            self.__append(val, self.root)
        else:
            self.root = BinarySearchTree.TreeNode(val)

    
    def __append(self,val,currentNode):
        if val is not None:
            if val < currentNode.val:
                if currentNode.hasLeftChild():
                    self.__append(val,currentNode.leftChild)
                else:
                    currentNode.leftChild = BinarySearchTree.TreeNode(val,parent=currentNode)
            
            else:
                if currentNode.hasRightChild():
                    self.__append(val,currentNode.rightChild)
                else:
                    currentNode.rightChild = BinarySearchTree.TreeNode(val,parent=currentNode)

    def __get(self,val,currentNode):
        if not currentNode:
            return None
        elif currentNode.val == val:
            return currentNode
        elif val < currentNode.val:
            return self.__get(val,currentNode.leftChild)
        else:
            return self.__get(val,currentNode.rightChild)
        

    def __contains__(self,val):
        if self.__get(val,self.root):
            return True
        else:
            return False    