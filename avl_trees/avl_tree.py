class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def get_height(self):
        pass

    def display(self):
        if self.key == None:
            print("NULL", end=" ")
            return 0
        print(self.key, end=" ")
        if self.left:
            self.left.display()
        else:
            print("NULL", end=" ")
        if self.right:
            self.right.display()
        else:
            print("NULL", end=" ")


class AVLTree():
    def __init__(self):
        self.root = None
    
    def display(self):
        if self.root:
            self.root.display()
            print()
    
    def insert_node(self, root, node):
        if not self.root:
            self.root = node
            return 0
        elif self.key > node.key:
            pass
        else:
            pass


def main():
    avl_tree = AVLTree()
    avl_tree.display()
    avl_tree.root = TreeNode(6)
    avl_tree.display()



main()