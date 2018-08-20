class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# preorder traversal of tree
def preorder(tree):
    if tree:
        print("{}".format(tree.data))
        preorder(tree.left)
        preorder(tree.right)

# inorder traversal of tree
def inorder(tree):
    if tree:
        preorder(tree.left)
        print("{}".format(tree.data))
        preorder(tree.right)

# postorder traversal of tree
def postorder(tree):
    if tree:
        preorder(tree.left)
        preorder(tree.right)
        print("{}".format(tree.data))

# level order / breadth first traversal of tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):
        # Print front of queue and remove it from queue
        print(queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\n Preorder Traversal of binary tree is -")
preorder(root)

print("\n inorder Traversal of binary tree is -")
inorder(root)

print("\n postorder Traversal of binary tree is -")
postorder(root)

print("\n Level Order / breadth first Traversal of binary tree is -")
printLevelOrder(root)
