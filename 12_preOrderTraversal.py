# Binary Trees
"""
    level 1      A
       right  /     \ left 
    level 2   B       C
              /\        |
    level 3   D E         F
            leaf Node
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

    def preOrder(self, start, records):
        if start is not None:
            records.append(start.value)
            records = self.preOrder(start.left, records) # recursion
            records = self.preOrder(start.right, records)

        return records

# Root -> Left subTree -> Right subTree

tree = Tree(TreeNode(5))
tree.root.left = TreeNode(3)
tree.root.right = TreeNode(4)
tree.root.left.left = TreeNode(2)
tree.root.left.right = TreeNode(8)

print(tree.preOrder(tree.root, []))


"""
        5   ->  [5, 3, 2, 8, 4]
       /  \
      3    4
     / \
    2   8 
"""

