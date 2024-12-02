class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        
    def insert(self,data):
        if data < self.operator():
            if self.left() is None:
                self.left() == Node(data, self)    
            else:
                self.left().insert(data)
        elif data > self.operator():
            if self.right() is None:
                self.right = Node(data,self)
            else:
                self.right().insert(data)
    def operator(self):
        return self.data
    def left(self):
        return self.left
    def right(self):
        return self.right  
    def parent(self):
        return self.parent
    