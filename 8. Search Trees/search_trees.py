from reference_classes.reference_search_trees import TreeMap, SplayTreeMap

# Question 1
print("1. Insert, into an empty binary search tree, entries with keys 30, 40, 24, 58, 48, 26, 25 (in this order). "
      "Draw the tree after each insertion.")
tree = TreeMap()

root = tree._add_root(30)
print('Root Element: ', root.element(), '\n')

node_40 = tree._add_right(root, 40)
print('Right of Root Element: ', tree.right(root).element())
node_24 = tree._add_left(root, 24)
print('Left of Root Element: ', tree.left(root).element(), '\n')

node_58 = tree._add_right(node_40, 58)
print('Right of Node 40 Element: ', tree.right(node_40).element())
node_48 = tree._add_left(node_58, 48)
print('Left of Node 58 Element: ', tree.left(node_58).element())

node_26 = tree._add_right(node_24, 26)
print('Right of Node 24 Element: ', tree.right(node_24).element())
node_25 = tree._add_left(node_26, 25)
print('Left of Node 26 Element: ', tree.left(node_26).element(), '\n')

print('Number of elements: ', len(tree), '\n')


# Question 2
print("\n2. (R-11.3) How many different binary search trees can store the keys {1,2,3}?")
print('Different Binary Trees \n')
print('Binary Tree 1')
tree = TreeMap()

root = tree._add_root(2)
print('Root Element: ', root.element())
node_3 = tree._add_right(root, 3)
print('Right of Root Element: ', tree.right(root).element())
node_1 = tree._add_left(root, 1)
print('Left of Root Element: ', tree.left(root).element(), '\n')

print('Binary Tree 2')
tree = TreeMap()

root = tree._add_root(1)
print('Root Element: ', root.element())
node_2 = tree._add_right(root, 2)
print('Right of Root Element: ', tree.right(root).element())
node_3 = tree._add_right(node_2, 3)
print('Right of Node 2 Element: ', tree.right(node_2).element(), '\n')

print('Binary Tree 3')
tree = TreeMap()

root = tree._add_root(3)
print('Root Element: ', root.element())
node_2 = tree._add_left(root, 2)
print('Left of Root Element: ', tree.left(root).element())
node_1 = tree._add_left(node_2, 1)
print('Left of Node 2 Element: ', tree.left(node_2).element(), '\n')

print('Binary Tree 4')
tree = TreeMap()

root = tree._add_root(3)
print('Root Element: ', root.element())
node_1 = tree._add_left(root, 1)
print('Left of Root Element: ', tree.left(root).element())
node_2 = tree._add_right(node_1, 2)
print('Right of Node 1 Element: ', tree.right(node_1).element(), '\n')

print('Binary Tree 5')
tree = TreeMap()

root = tree._add_root(1)
print('Root Element: ', root.element())
node_3 = tree._add_right(root, 3)
print('Right of Root Element: ', tree.right(root).element())
node_2 = tree._add_left(node_3, 2)
print('Left of Node 3 Element: ', tree.left(node_3).element(), '\n')


# Question 3
print("\n3. Draw an AVL tree resulting from the insertion of an entry with key 52 into the AVL tree below:")
# Initial Tree
avl_tree = TreeMap()

root = avl_tree._add_root(62)
print('Initial Tree: \n')
print('Root Element: ', root.element(), '\n')

node_78 = avl_tree._add_right(root, 78)  # First Right subtree
node_88 = avl_tree._add_right(node_78, 88)  # Right Child of first right subtree
print('Right of Root Element: ', avl_tree.right(root).element())
print('Right of Node 78 Element: ', avl_tree.right(node_78).element(), '\n')

node_44 = avl_tree._add_left(root, 44)  # First Left subtree
node_17 = avl_tree._add_left(node_44, 17)  # Left child of first left subtree
node_50 = avl_tree._add_right(node_44, 50)  # Right child of first left subtree, start of second left subtree
print('Left of Root Element: ', avl_tree.left(root).element())
print('Left child of first left subtree: ', avl_tree.left(node_44).element())
print('Right child of first left subtree: ', avl_tree.right(node_44).element(), '\n')

node_48 = avl_tree._add_left(node_50, 48)  # Left child of second left subtree
node_54 = avl_tree._add_right(node_50, 54)  # Right child of second left subtree
print('Left child of second left subtree: ', avl_tree.left(node_50).element())
print('Right child of second left subtree: ', avl_tree.right(node_50).element(), '\n')

print('Insert key 52:')
node_52 = avl_tree._add_left(node_54, 52)
print('Left child of third left subtree: ', avl_tree.left(node_54).element())

print('Restructure tree:', '\n')
avl_tree._restructure(node_54)

print('Display left path for restructured Tree \n')
print('Root Element:', root.element())
print('Left of Root Element:', avl_tree.left(root).element(), '\n')
print('Left child of first left subtree:', avl_tree.left(node_50).element())
print('Right child of first left subtree:', avl_tree.right(node_50).element(), '\n')

print('Left grandchild of first left subtree on left side', avl_tree.left(node_44).element())
print('Right grandchild of first left subtree on left side:', avl_tree.right(node_44).element(), '\n')

print('Left grandchild of first left subtree on right side:', avl_tree.left(node_54).element())


# Question 4
print("\n4. Insert into an empty splay tree entries with keys 10, 16, 12, 14, 13 (in this order). Draw the tree after "
      "each insertion.")
splay = SplayTreeMap()

print('Stage 1: Add Root')
root = splay._add_root(10)
print('Root node added:', root.element(), '\n')

print('Stage 2: Insert 16')
node16 = splay._add_right(root, 16).element()
pos16 = splay.right(root)
print('Right node of root added:', splay.right(root).element(), '\n')

splay._splay(pos16)
print('Splaying.. \n')

new_root = splay.root().element()
left_root = splay.left(splay.root()).element()
print('Root node:', new_root )
print('Left of root node:', left_root, '\n')

print('Stage 3: Insert 12')
node12 = splay._add_right(splay.left(splay.root()), 12).element()
pos12 = splay.right(splay.left(splay.root()))
print('Node added:', node12, '\n')

splay._splay(pos12)
print('Splaying.. \n')


new_root = splay.root().element()
left_root = splay.left(splay.root()).element()
right_root = splay.right(splay.root()).element()
print('Root node:', new_root )
print('Left of root node:', left_root)
print('Right of root node:', right_root, '\n')

print('Stage 4: Insert 14')
node14 = splay._add_left(splay.right(splay.root()), 14).element()
pos14 = splay.left(splay.right(splay.root()))
print('Node added:', node14, '\n')

splay._splay(pos14)
print('Splaying.. \n')

new_root = splay.root().element()
left_root = splay.left(splay.root()).element()
right_root = splay.right(splay.root()).element()
left_grandchild_root = splay.left(splay.left(splay.root())).element()

print('Root node:', new_root )
print('Left of root node:', left_root)
print('Right of root node:', right_root)
print('Left grandchild of root node:', left_grandchild_root, '\n')


print('Stage 5: Insert 13')
node13 = splay._add_right(splay.left(splay.root()), 13).element()
pos13 = splay.right(splay.left(splay.root()))
print('Node added:', node13, '\n')

splay._splay(pos13)
print('Splaying.. \n')

new_root = splay.root().element()
left_root = splay.left(splay.root()).element()
right_root = splay.right(splay.root()).element()
left_grandchild_root = splay.left(splay.left(splay.root())).element()
right_grandchild_root = splay.right(splay.right(splay.root())).element()

print('Root node:', new_root )
print('Left of root node:', left_root)
print('Right of root node:', right_root)
print('Left grandchild of root node:', left_grandchild_root)
print('Right grandchild of root node:', right_grandchild_root)


