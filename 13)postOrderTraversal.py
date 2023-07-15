class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

    def preOrder(self, start, records):
        if start is not None:
            records.append(start.value) # Root
            records = self.preOrder(start.left, records) # Left subTree first
            records = self.preOrder(start.right, records) # Right subTree second

        return records

    def postOrder(self, start, records):
        if start is not None:
            records = self.postOrder(start.left, records)  # Left subTree first
            records = self.postOrder(start.right, records) # Right subTree second
            records.append(start.value) # Finally add the current node to list of nodes
        
        return records
    
tree = Tree(Node(5))
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(2)
tree.root.left.right = Node(8)
print("Pre Order Traversal")
print(tree.preOrder(tree.root, [] )) #[5, 3, 2, 8, 4]

print("Post Order Traversal")
print(tree.postOrder(tree.root, [])) #[2, 8, 3, 4, 5]