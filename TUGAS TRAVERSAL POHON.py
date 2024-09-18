from __future__ import print_function

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items==[]

    def push(self,items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
   
class Binarytree:
    def __init__(self,root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None :
            self.leftChild = Binarytree(newNode)

        else :
            t = Binarytree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None :
            self.rightChild = Binarytree(newNode)

        else :
            t = Binarytree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getrightChild(self):
        return self.rightChild

    def getleftChild(self):
        return self.leftChild

    def getrootVal(self):
        return self.key

    def setrootVal(self,obj):
        self.key = obj

    def size(self):
        count = 0
        selfleft = self
        selfright = self
        while selfleft.getleftChild() != None or selfright.getrightChild() != None :
            count += 1
            if selfleft.getleftChild() != None:
                selfleft = selfleft.getleftChild()
            else :
                selfright = selfright.getrightChild()
        return count

def Inorder(root):
    if root:
        Inorder(root.getleftChild())
        print(root.getrootVal(),end=" ")
        Inorder(root.getrightChild())

def Preorder(root):
    if root:
        print(root.getrootVal(),end=" ")
        Preorder(root.getleftChild())
        Preorder(root.getrightChild())

def Postorder(root):
    if root:
        Postorder(root.getleftChild())
        Postorder(root.getrightChild())
        print(root.getrootVal(),end=" ")

root = Binarytree('DANI')
root.insertLeft('SANTI')
root.getleftChild().insertLeft('FANI')
root.getleftChild().insertRight('REKA')
root.getleftChild().getleftChild().insertLeft('WATI')
root.getleftChild().getrightChild().insertRight('HADI')
root.insertRight('AMA')
root.getrightChild().insertLeft("MAMI")
root.getrightChild().insertRight("CICA")
Inorder(root)
print ()
Preorder(root)
print ()
Postorder(root)