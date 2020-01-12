class Node:

    #make constructor for insert data
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
    
    #insert item based on root
    def insertTree(self, root, node):
        if root is None: 
            root = node
        else:
            #insert value to right
            if root.value < node.value: 
                if root.right is None:
                    root.right = node
                else:
                    self.insertTree(root.right, node)
            if root.value > node.value:
                if root.left is None: 
                    root.left = node
                else: 
                    self.insertTree(root.left, node)

    # will print tree
    def tree(self, root):
        if root:
            self.tree(root.left)
            print(root.value)
            self.tree(root.right)

root = Node(40)
root.insertTree(root, Node(10))
root.insertTree(root, Node(15))
root.insertTree(root, Node(9))
root.insertTree(root, Node(6))
root.insertTree(root, Node(24))
root.insertTree(root, Node(32))

root.tree(root)