def bfs(self, root=None):
  if root is None:
    return
  queue = [root]
  while len(queue) > 0:
    cur_node = queue.pop(0)
    if cur_node.left is not None:
      queue.append(cur_node.left)
    if cur_node.right is not None:
      queue.append(cur_node.right)
  print(queue)
