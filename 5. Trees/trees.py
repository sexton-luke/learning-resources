from reference_classes.reference_trees import LinkedBinaryTree

# Initial Tree and Root Node
tree = LinkedBinaryTree()
root = tree._add_root(1)

# Add Left Subtree
node_2 = tree._add_left(root, 2)
tree._add_left(node_2, 4)
tree._add_right(node_2, 5)

# Add Right Subtrees
node_3 = tree._add_right(root, 3)
node_6 = tree._add_left(node_3, 6)
node_7 = tree._add_right(node_3, 7)

tree._add_left(node_6, 8)
tree._add_right(node_6, 9)

tree._add_left(node_7, 10)
print('Number of elements: ', len(tree), '\n')

# Print Node Elements
print('Root Element: ', root.element(), '\n')
print('Left of Root Element (Node 2): ', tree.left(root).element())
print('Right of Root Element (Node 3): ', tree.right(root).element(), '\n')

print('Left of Node 2 Element (Node 4): ', tree.left(node_2).element())
print('Right of Node 2 Element (Node 5): ', tree.right(node_2).element(), '\n')

print('Left of Node 3 Element (Node 6): ', tree.left(node_3).element())
print('Right of Node 3 Element (Node 7): ', tree.right(node_3).element(), '\n')

print('Left of Node 6 Element (Node 8): ', tree.left(node_6).element())
print('Right of Node 6 Element (Node 9): ', tree.right(node_6).element(), '\n')

print('Left of Node 7 Element (Node 10): ', tree.left(node_7).element())
