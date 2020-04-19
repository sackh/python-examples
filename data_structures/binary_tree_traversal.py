
class TreeNode:
    """
     Node of Binary Tree
    """
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def inorder_iterative(root):
    """
     Inorder trversal iterative function
    :param root:
    :return:
    """
    temp = root
    stack = []
    while True:
        while temp:
            stack.append(temp)
            temp = temp.left
        if not stack:
            break
        temp = stack.pop()
        print(temp.data, end=' ')
        temp = temp.right


def inorder_recursive(root):
    """
     Recursive method for inorder traversal
    :param root:
    :return:
    """
    if root:
        inorder_recursive(root.left)
        print(root.data, end=' ')
        inorder_recursive(root.right)


def preorder_iterative(root):
    """
     Pre order traversal iterative method
    :param root:
    :return:
    """
    temp = root
    stack = []
    while True:
        while temp:
            stack.append(temp)
            print(temp.data, end=' ')
            temp = temp.left
        if not stack:
            break
        temp = stack.pop()
        temp = temp.right


def preorder_recursive(root):
    if root:
        print(root.data, end=' ')
        preorder_recursive(root.left)
        preorder_recursive(root.right)


if __name__ == "__main__":
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('c')
    root.left.left = TreeNode('d')
    root.left.right = TreeNode('e')
    root.right.left = TreeNode('f')
    root.right.right = TreeNode('g')
    print('inorder traversal')
    inorder_iterative(root)
    print()
    inorder_recursive(root)
    print()
    print('preorder traversal')
    preorder_iterative(root)
    print()
    preorder_recursive(root)
