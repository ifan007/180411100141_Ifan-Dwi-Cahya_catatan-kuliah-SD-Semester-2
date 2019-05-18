class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key=obj

    def getRootVal(self):
        return self.key

    def show(self):
        current=self.key
        print(current)

        selfleft=self
        selfright=self
        while selfleft.getLeftChild()!=None and selfright.getRightChild() !=None:
            print (selfleft.getLeftChild().getRootVal())
            print (selfright.getRightChild().getRootVal())

            selfleft=selfleft.getLeftChild()
        while selfright.getRightChild()!=None:
            print(selfright.getRightChild().getRootVal())

            selfright=selfright.getRightChild()

    def height(self):
        selfleft=self
        selfright=self
        count=0
        while selfleft.getLeftChild()!=None or selfright.getRightChild()!=None:
            count+=1
            if selfleft.getLeftChild()!=None:
                selfleft=selfleft.getLeftChild()

            if selfright.getRightChild()!=None:
                selfright=selfright.getRightChild()
        return count

r=BinaryTree('a')
print (r.getRootVal())

r.insertLeft('b')
r.insertRight('c')

print (r.getLeftChild().getRootVal())

print (r.getRightChild().getRootVal())
print (r.height())
