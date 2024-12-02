from node import Node
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def size(self):
        return self.size
    def empty(self):
        return self.size == 0
    def printNodes(self):
        self.inorder(self.root)
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)
    def add(self, data):
        if self.root is None:
            self.root = Node(data, None)
            self.size += 1
        else:
            self.size += 1
            
BT= BinaryTree()
BT.add(10)
BT.add(5)
BT.add(7)
BT.add(1)
BT.printNodes()