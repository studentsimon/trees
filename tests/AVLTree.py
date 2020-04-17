from Trees.BinaryTree import BinaryTree, Node
from Trees.BST import BST

class AVLTree():
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        self.root = None
        if xs:
            self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)


    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance fa$
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        return AVLTree._balance_factor(node) in [-1,0,1] and AVLTree._is_avl_satisfied(node.left) and AVLTree._is_avl_satisfied(node.right)

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly differ$
        however, so you will have to adapt their code.
        '''

        if node is None or node.right is None:
            return node
        new_node = Node(node.right.value)
        new_node.right = node.right.left
        new_left = Node(node.value)
        new_left.left = node.left
        new_left.right = node.right.left
        new_node.left = new_left
        return new_node


    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly differ$
        however, so you will have to adapt their code.
        '''

        if node is None or node.right is None:
            return node
        new_node = Node(node.left.value)
        new_node.left = node.left.left
        new_right = Node(node.value)
        new_right.right = node.right
        new_right.left = node.left.right
        new_node.right = new_right
        return new_node


    def insert(self, value):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(value,self.root)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''


        for i in xs:
            self.insert(i)
     
    @staticmethod        
    def _rebalance(node):


        if AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)

            else:
                return AVLTree._right_rotate(node)

        elif AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)

            else:
                return AVLTree._left_rotate(node)

        else:

            return node

    @staticmethod
    def _insert(value, node):

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                AVLTree._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                AVLTree._insert(value, node.right)
        else:
            print("Here already.")




        if not AVLTree._is_avl_satisfied(node):
            node.left = AVLTree._rebalance(node.left)
            node.right = AVLTree._rebalance(node.right)
            return AVLTree._rebalance(node)
        else:
            return node


#new

from Trees.BinaryTree import BinaryTree, Node

class BST(BinaryTree):
    '''
    FIXME:
    BST is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        self.root = None
        if xs != None:
            self.insert_list(xs)


    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"
        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of BST will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__+'('+str(self.to_list('inorder'))+')'


    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        Implement this method.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        

        right_valid = True
        left_valid = True


        if node.right:
            right_valid = node.value < node.right.value and BST._is_bst_satisfied(node.right)

        if node.left:
            left_valid = node.value > node.left.value and BST._is_bst_satisfied(node.left)

        return left_valid and right_valid


    def insert(self, value):
        '''
        Inserts value into the BST.
        '''
        if self.root is None:
            self.root = Node(value)
        elif self.root != None:
            BST._insert(value, self.root)


    @staticmethod
    def _insert(value, node):
        '''
        FIXME:
        Implement this function.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                BST._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                BST._insert(value, node.right)
        else:
            print("Value is already present in tree.")



    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''


        for i in xs:
            self.insert(i)


    def __contains__(self, value):
        return self.find(value)


    def find(self, value):
        '''
        Returns whether value is contained in the BST.
        '''
        if self.root:
            if BST._find(value, self.root):
                return True
        else:
            return False


    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        if value > node.value and node.right:
            return BST._find(value, node.right)
        elif value < node.value and node.left:
            return BST._find(value, node.left)

        if value == node.value:
            return True


    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a BST it should be easy to implement.
        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''

        if self.root:
            return BST._find_smallest(self.root)
        return None
    
    @staticmethod
    def _find_smallest(node):
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.
        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a BST it should be easy to implement.
        '''

        if self.root:
            return BST._find_largest(self.root)
        return None

    @staticmethod
    def _find_largest(node):
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)


    def remove(self,value):
        '''
        Removes value from the BST. 
        If value is not in the BST, it does nothing.
        FIXME:
        implement this function.
        There is no code given in any of the lecture videos on how to implement this function,
        but the video by HMC prof Colleen Lewis explains the algorithm.
        HINT:
        You must have find_smallest/find_largest working correctly 
        before you can implement this function.
        HINT:
        Use a recursive helper function.
        '''

        self.root = BST._remove(self.root,value)

    @staticmethod
    def _remove(node, value):
        if not node:
            return node

        if node.value > value:

            node.left=BST._remove(node.left, value)

        elif node.value < value:

            node.right = BST._remove(node.right, value)

        else:

            if not node.left:
                return node.right

            if not node.right:
                return node.left

            tmp = node.right
            while tmp.left:
                tmp = tmp.left

            node.value = tmp.value
            node.right = BST._remove(node.right, node.value)

        return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.
        FIXME:
        Implement this function.
        '''
        for i in xs:
            self.remove(i)


class Node():
    '''
    You do not have to implement anything within this class.
    Given a node t, you can visualize the node by running str(t) in the python interpreter.
    This is a key method to perform debugging,
    so you should get familiar with how to visualize these strings.
    '''
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        ret = '('
        ret += str(self.value)
        ret += ' - '
        if self.left:
            ret += str(self.left)
            ret += ' '
        ret += '- '
        if self.right:
            ret += str(self.right)
            ret += ' '
        ret += ')'
        return ret


class BinaryTree():
    '''
    This class is relatively useless by itself,
    but it is the superclass for the BST, AVLTree, and Heap classes,
    and it provides important helper functions for these classes.
    If you don't implement all of the functions in this class correctly,
    it will be impossible to implement those other classes.
    '''

    def __init__(self, root=None):
        '''
        My version of this function is slightly modified from the video notes.
        I give the root variable a default value of None,
        which allows us to create a BinaryTree that has no elements within it.
        '''
        if root:
            self.root = Node(root)
        else:
            self.root = None

    def __str__(self):
        '''
        We can visualize a tree by visualizing its root node.
        '''
        return str(self.root)

    def print_tree(self, traversal_type):
        '''
        This function is taken from the lecture notes videos (almost) verbatim.
        The difference is that when an incorrect input is given,
        my version raises a ValueError rather than "failing silently".
        It is always good practice to make errors as loud and explicit as possible,
        as this will reduce the effort you need for debugging.
        '''
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        else:
            raise ValueError('Traversal type ' + str(traversal_type) + ' is not supported.')

    def preorder_print(self, start, traversal):
        '''
        FIXME: 
        Implement this function.
        The lecture notes videos provide the exact code you need.
        '''
        ''' Root -> Left -> Right'''



        if start:

            traversal += (str(start.value) + "-")
            
            traversal = self.preorder_print(start.left, traversal)

            traversal = self.preorder_print(start.right, traversal)

        return traversal

    def inorder_print(self, start, traversal):
        '''
        FIXME: 
        Implement this function.
        The lecture notes videos provide the exact code you need.
        '''
        ''' Left -> Root -> Right'''

        if start:

            traversal = self.inorder_print(start.left, traversal)

            traversal += (str(start.value) + "-")

            traversal = self.inorder_print(start.right, traversal)

        return traversal

    def postorder_print(self, start, traversal):
        '''
        FIXME: 
        Implement this function.
        The lecture notes videos provide the exact code you need.
        '''
        ''' Left -> Right -> Root'''
        if start:

            traversal = self.postorder_print(start.left, traversal)

            traversal = self.postorder_print(start.right, traversal)

            traversal += (str(start.value) + "-")

        return traversal


    def to_list(self, traversal_type):
        '''
        This function is similar to the print_tree function,
        but instead of printing the tree,
        it returns the contents of the tree as a list.
        A general programming principle is that a function should return its results 
        rather than print them whenever possible.
        If a function returns its results,
        we can always print the returned results if we need to visualize them.
        But by returning the results we can also do more computations on the results if needed.
        Many of the test cases for more complicated tree functions rely on this to_list function,
        so it is import to implement it correctly.
        '''
        if traversal_type == 'preorder':

            return self.preorder(self.root, [])

        elif traversal_type == 'inorder':

            return self.inorder(self.root, [])

        elif traversal_type == 'postorder':

            return self.postorder(self.root, [])

        else:

            raise ValueError('traversal_type=' + str(traversal_type) + ' is not supported.')

    def preorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        if start: #modifying the upper version "preorder_print"
            traversal.append(start.value) 
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal.append(start.value)
            traversal = self.inorder(start.right, traversal)
        return traversal 

    def postorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal.append(start.value)
        return traversal

    def __len__(self):
        '''
        The lecture notes videos provide a recursive and an iterative version of a "size" function
        which behaves the same as the __len__ function is supposed to.
        You may copy that code here exactly.
        We are using the dunder method __len__ because that will allow us to use the len() function
        on our BinaryTree instances.
        '''
        return self.size_(self.root)

    def size(self):
        '''
        FIXME:
        Implement this function. 
        The lecture notes videos provide the exact code you need.
        '''
        if self.root is None:
            return 0

        stack = []
        stack.append(self.root)

        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.append(node.left)
            if node.right:
                size += 1
                stack.append(node.right)
        return size

    def size_(self, node):
        '''
        FIXME:
        Implement this function.
        The lecture notes videos provide the exact code you need.
        '''

        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)

    def height(self):
        return BinaryTree._height(self.root)

    @staticmethod
    def _height(node):
        '''
        FIXME:
        Implement this function. 
        The lecture notes videos provide (almost) the exact code you need.
        In the video, the function is not implemented as a static function,
        and so the self argument is passed in as the first argument of height.
        This makes it inconvenient to use,
        and so you should implement it as a static method.
        '''

        if node is None:
            return -1
        right_height = BinaryTree._height(node.right)
        left_height = BinaryTree._height(node.left)

        return max(left_height, right_height) + 1



