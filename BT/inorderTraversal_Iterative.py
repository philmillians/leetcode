class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def inorderIterative(root):
  stack = []
  currentNode = root
  while stack or currentNode:
    if currentNode:
      stack.append(currentNode)
      currentNode = currentNode.left
    else:       
      currentNode = stack.pop()
      print(currentNode.data, end=' ')
      currentNode = currentNode.right
 
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
 
    inorderIterative(root)
