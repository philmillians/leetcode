class Node:
  def __init__(self,value):
    self.value=value
    self.right=None
    self.left=None

def inOrderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.value, end=' ')
    inOrderTraversal(root.right)

if __name__ == '__main__':
 
    ''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    inOrderTraversal(root)
 
