class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return self.root
        current = self.root
        while True:
            if current.value > value:
                if not current.left:
                    current.left = node
                    return True
                else: 
                    current = current.left
            elif current.value < value:
                if not current.right:
                    current.right = node
                    return True
                else: 
                    current = current.right
            else:
                return None
   
    def pre_order(self):
        current = self.root
        def traverse(node):
            print(node.value)
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
        traverse(current)
        return True

    def post_order(self):
        current = self.root
        def traverse(node):
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
            print(node.value)
        traverse(current)
        return True

    def in_order(self):
        current = self.root
        def traverse(node):
            if node.left: traverse(node.left)
            print(node.value) 
            if node.right: traverse(node.right)
        traverse(current)
        return True
    
  

if __name__ == "__main__":
    bt = BinarySearchTree()
    bt2 = BinarySearchTree()
    bt.insert(3)
    bt.insert(4)
    bt.insert(1)
    bt2.insert(3)
    bt2.insert(2)