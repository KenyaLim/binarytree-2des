class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent= parent
        self.left = None
        self.right = None
    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data,self)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data,self)
            else:
                self.right.insert(data)
        else:
            return False
        return True
    
    class BinaryTree:
        def __init__(self):
            self.root = None
            self.size = 0
        def add(self,data):
            if self.root.left is None and data%2 != 0:
                self.root.left = Node(data,self.root)
            elif self.root.right is None and data%2 == 0:
                self.root.right = Node(data,self.root)
        def sumGanjil(self, node,ganjil=[]):
            if node is not None:
                if node.data % 2 != 0 :
                    ganjil.append(node.data)
                self.sumGanjil(node.left, ganjil)
                self.sumGanjil(node.right, ganjil)
            return ganjil
        def sumGenap(self, node, genap=[]):
            if node is not None:
                if node.data % 2 == 0 :
                    genap.append(node.data)
                self.sumGenap(node.left, genap)
                self.sumGenap(node.right, genap)
            return genap
        def hasilGanjil(self):
            hasil_ganjil = self.sumGanjil(self.root.left, [])
            return f"Hasil: {sum(hasil_ganjil)}"
        def hasilGenap(self):
            hasil_genap = self.sumGenap(self.root.right, [])
            return f"Hasil: {sum(hasil_genap)}"
        
if __name__ == "__main

bt = BinaryTree()
bt.add(5)
bt.add(3)
            