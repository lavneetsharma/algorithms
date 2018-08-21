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

# function to find diagonal traversal
def diagonalPrintUtil(root, d, diagonalPrintMap):
    # Base Case
    if root is None:
        return

    # Store all nodes of same line together as a vector
    try :
        diagonalPrintMap[d].append(root.data)
    except KeyError:
        diagonalPrintMap[d] = [root.data]

    # Increase the vertical distance if left child
    diagonalPrintUtil(root.left, d+1, diagonalPrintMap)

    # Vertical distance remains same for right child
    diagonalPrintUtil(root.right, d, diagonalPrintMap)

# diagonal traversal of tree
def diagonalPrint(root):

    # Create a dict to store diagnoal elements
    diagonalPrintMap = dict()

    # Find the diagonal traversal
    diagonalPrintUtil(root, 0, diagonalPrintMap)

    for i in diagonalPrintMap:
        for j in diagonalPrintMap[i]:
            print(j)

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

print("\n Diagonal Traversal of binary tree is -")
diagonalPrint(root)
