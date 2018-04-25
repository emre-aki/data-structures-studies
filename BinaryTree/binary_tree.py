"""
#TODO: Improve triple quote comments on utility functions.
"""

from Queue.queue import Queue
from BinaryTree.node import Node
from copy import deepcopy

class BinaryTree:

    def __init__(self):
        self.__root = None

    def append(self, data):
        """
        Inserts a new node with the given value to the Binary Tree.
        """
        new_node = Node(data)
        if self.is_empty():
            self.__root = new_node
        else:
            q = Queue()
            q.push(self.__root)
            inserted = False
            while not inserted:
                curr_node = q.pop()
                if curr_node.left is None:
                    curr_node.left = new_node
                    inserted = True # insertion to tree is complete, so break
                elif curr_node.right is None:
                    curr_node.right = new_node
                    inserted = True # insertion to tree is complete, so break
                else: # if the current node is full, proceed with their children
                    q.push(curr_node.left)
                    q.push(curr_node.right)

    def find(self, data):
        """
        Checks whether given a node with the given data is present in the tree.
        Return `True` if any such node exists, `False` otherwise. 
        """
        return self.__alt_find_node(self.__root, data)

    def __find_node(self, node, data):
        """
        A private utility function for `BinaryTree.find` to traverse the Binary Tree
        in order to check whether a node with the given value is present.
        """
        if node is None:
            return False
        elif node.data == data:
            return True
        return self.__find_node(node.left, data) or self.__find_node(node.right, data)

    def __alt_find_node(self, node, data):
        """
        Identical to `BinaryTree.__find_node`
        A private utility function for `BinaryTree.find` to traverse the Binary Tree
        in order to check whether a node with the given value is present.
        """
        if node is None:
            return False
        if node.data == data:
            return True
        found = self.__alt_find_node(node.left, data)
        if found:
            return found
        return self.__alt_find_node(node.right, data)

    def get_root(self):
        """
        Returns the root node of the Binary Tree.
        """
        if not self.is_empty():
            return self.__root.data
        return None

    def get_leaves(self):
        """
        Returns all the leaf nodes in the Binary Tree in a list.
        """
        result = []
        if not self.is_empty():
            self.__find_leaves(self.__root, result)
        return result

    def __find_leaves(self, node, result):
        """
        A utility function for `BinaryTree.get_leaves` to traverse the tree
        in order to find its leaf nodes.
        """
        if node.left is None and node.right is None:
            result.append(node)
        else:
            if node.left is not None:
                self.__find_leaves(node.left, result)
            if node.right is not None:
                self.__find_leaves(node.right, result)

    def from_list(self, list):
        """
        Constructs a BinaryTree object from the given list.
        """
        cp_list = deepcopy(list)
        self.__root = Node(cp_list[0])
        cp_list.pop(0)
        for elem in cp_list:
            self.append(elem)

    def to_list(self):
        """
        Converts the BinaryTree instance to a Python list.
        """
        return self.breadth_first()

    def breadth_first(self):
        """
        Traverses the BinaryTree one level at a time. Each node visited is
        collected in a list, which then is returned.
        """
        result = []
        if not self.is_empty():
            q = Queue()
            q.push(self.__root)
            while not q.is_empty():
                curr_node = q.pop()
                result.append(curr_node)
                if curr_node.left is not None:
                    q.push(curr_node.left)
                if curr_node.right is not None:
                    q.push(curr_node.right)
        return result

    def traverse(self, ttype='preorder'):
        """
        Traverses the BinaryTree as specified in the named argument `ttype`.
        The default is preorder. Each node visited is collected in a list,
        which then is returned.
        """
        result = []
        if not self.is_empty():
            if ttype == 'preorder':
                self.__traverse_preorder(self.__root, result)
            elif ttype == 'inorder':
                self.__traverse_inorder(self.__root, result)
            elif ttype == 'postorder':
                self.__traverse_postorder(self.__root, result)
        return result

    def __traverse_preorder(self, node, result):
        """
        Utility function for BinaryTree.traverse. Traverses the BinaryTree in preorder.
        Each node visited is collected in a list, which then is returned.
        """
        result.append(node)
        if node.left is not None:
            self.__traverse_preorder(node.left, result)
        if node.right is not None:
            self.__traverse_preorder(node.right, result)

    def __traverse_inorder(self, node, result):
        """
        Utility function for BinaryTree.traverse. Traverses the BinaryTree in inorder.
        Each node visited is collected in a list, which then is returned.
        """
        if node.left is not None:
            self.__traverse_inorder(node.left, result)
        result.append(node)
        if node.right is not None:
            self.__traverse_inorder(node.right, result)

    def __traverse_postorder(self, node, result):
        """
        Utility function for BinaryTree.traverse. Traverses the BinaryTree in postorder.
        Each node visited is collected in a list, which then is returned.
        """
        if node.left is not None:
            self.__traverse_postorder(node.left, result)
        if node.right is not None:
            self.__traverse_postorder(node.right, result)
        result.append(node)

    def depth(self):
        """
        Returns the maximum depth in the BinaryTree.
        """
        return self.__compute_depth(self.__root)

    def __compute_depth(self, node):
        """
        Utility function for BinaryTree.depth.
        Returns the maximum depth in the BinaryTree.
        """
        if node is None:
            return 0
        return (max(self.__compute_depth(node.left), self.__compute_depth(node.right)) + 1)

    def min_depth(self):
        """
        Returns the minimum depth in the BinaryTree.
        """
        return self.__compute_min_depth(self.__root)

    def __compute_min_depth(self, node):
        """
        Utility function for BinaryTree.depth.
        Returns the maximum depth in the BinaryTree.
        """
        if node is None:
            return 0
        return (min(self.__compute_min_depth(node.left), self.__compute_min_depth(node.right)) + 1)

    def get_depths(self):
        """
        Traverses the BinaryTree while collecting the depth
        of each node into a list. This list is then returned.
        """
        if not self.is_empty():
            depths = [0] * self.__len__()
            self.__construct_depth_array(depths, [0], self.__root, 1)
            return depths
        return []

    def __construct_depth_array(self, array, idx, node, depth):
        """
        Utility function for BinaryTree.get_depths.
        Traverses the BinaryTree while collecting the depth
        of each node in a list. This list is then returned.
        """
        array[idx[0]] = depth
        idx[0] += 1
        if node.left is not None:
            self.__construct_depth_array(array, idx, node.left, depth + 1)
        if node.right is not None:
            self.__construct_depth_array(array, idx, node.right, depth + 1)

    def depth_of_deepest(self, data):
        """
        Returns the depth of the node having the maximum depth that has the given data.

        This algorithm performs a linear traversal over a depth array returned from
        BinaryTree.__construct_depth_array. Thus, it has a worst case computational complexity
        of `O(n)`.
        """
        preorder = self.traverse()
        depths = self.get_depths()
        max_depth = 0
        for (i, node) in enumerate(preorder):
            if node.data == data and depths[i] > max_depth:
                max_depth = depths[i]
        return max_depth

    def alt_depth_of_deepest(self, data):
        """
        Identical to BinaryTree.depth_of_the_deepest.
        Returns the depth of the node having the maximum depth that has the given data.

        This algorithm performs a breadth-first traversal over the BinaryTree instance,
        and calls BinaryTree.depth_of_first for each node in the tree. Thus, it has a
        worst case computational complexity of `O(n^2)`.
        """
        if not self.is_empty():
            max_depth = 0
            q = Queue()
            q.push(self.__root)
            while not q.is_empty():
                curr_node = q.pop()
                curr_depth = self.depth_of_first(curr_node)
                if curr_node.data == data and max_depth < curr_depth:
                    #print('A \'%s\' is found; its depth: %d'%(str(curr_node.data), curr_depth))
                    max_depth = curr_depth
                if curr_node.left is not None:
                    q.push(curr_node.left)
                if curr_node.right is not None:
                    q.push(curr_node.right)
            return max_depth
        return -1

    def depth_of_first(self, data):
        """
        Returns the depth of the first occurrence of the node that has the given data.
        The input argument `data` also accepts BinaryTree.node.Node instances.
        """
        return self.__count_depth_of_first(self.__root, data, 1)

    def __count_depth_of_first(self, node, data, depth):
        """
        Utility function for Binary.depth_of_the_first.
        Returns the depth of the first occurrence of the node that has the given data.
        The input argument `data` also accepts BinaryTree.node.Node instances.
        """
        if node is None:
            return 0
        if (isinstance(data, Node) and node == data) or (node.data == data):
            return depth
        subtree_depth = self.__count_depth_of_first(node.left, data, depth + 1)
        if subtree_depth != 0:
            return subtree_depth
        return self.__count_depth_of_first(node.right, data, depth + 1)

    def __len__(self):
        """
        Returns the number of nodes, i.e., the length, in the BinaryTree instance
        """
        count = [0]
        self.__count_nodes(self.__root, count)
        return count[0]

    def __count_nodes(self, node, count):
        """
        Utility function for BinaryTree.__len__.
        Returns the number of nodes, i.e., the length, in the BinaryTree instance
        """
        count[0] += 1
        if node.left is not None:
            self.__count_nodes(node.left, count)
        if node.right is not None:
            self.__count_nodes(node.right, count)

    def __repr__(self):
        """
        Returns string representation for the BinaryTree instance.
        """
        return ('%r'%(self.breadth_first()))

    def __str__(self):
        """
        Returns string representation for the BinaryTree instance.
        Identical to BinaryTree.__repr__.
        """
        return ('%s'%(self.breadth_first()))

    def is_empty(self):
        """
        Helps determine whether the BinaryTree instance is empty or not.
        Returns a boolean value of `True` if empty, `False` otherwise.
        """
        return self.__root is None

    def is_saturated(self):
        """
        Helps determine whether the BinaryTree instance is saturated or not.
        Saturation in the tree is defined in terms of the number of children
        a node has. If all nodes in the tree has an even number of children,
        then it is said to be saturated.

        Returns a boolean value of `True` if saturated, `False` otherwise.
        """
        return self.__determine_if_saturated(self.__root)

    def __determine_if_saturated(self, node):
        """
        Utility function for BinaryTree.__is_saturated.
        Returns a boolean value of `True` if saturated, `False` otherwise.
        """
        if node is None:
            return True
        else:
            if not ((node.left is None and node.right is None)
                     or (node.left is not None and node.right is not None)):
                return False
            else:
                return (self.__determine_if_saturated(node.left) and self.__determine_if_saturated(node.right))