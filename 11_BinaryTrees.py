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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init(self, root):
        self.root = root

tree = Tree(5)
tree.root.left = TreeNode(3)
tree.root.right = TreeNode(4)

"""
        5
       /  \
      3    4

"""

