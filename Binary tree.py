class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')


root = Node(21)
root.insert(14)
root.insert(28)
root.insert(11)
root.insert(18)
root.insert(25)
root.insert(32)
root.insert(15)
root.insert(19)
root.insert(30)
print(root.PreorderTraversal(root))
print(root.findval(400))
print(root.findval(12))
print(root.findval(18))
print(root.findval(21))
print(root.findval(28))
