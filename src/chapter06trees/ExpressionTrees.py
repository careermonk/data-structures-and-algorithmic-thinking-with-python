# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

operatorPrecedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}
 
def postfixConvert(infix):
    stack = []
    postfix = [] 
         
    for char in infix:
        if char not in operatorPrecedence:
            postfix.append(char)
        else:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack[len(stack) - 1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()
                elif operatorPrecedence[char] > operatorPrecedence[stack[len(stack) - 1]]:
                    stack.append(char)
                else:
                    while len(stack) != 0:
                        if stack[len(stack) - 1] == '(':
                            break
                        postfix.append(stack.pop())
                    stack.append(char)
     
    while len(stack) != 0:
        postfix.append(stack.pop())
 
    return postfix
 
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class ExressionTree(object):
    def __init__(self, root=None):
        self.__root = root 
     
    def inorder(self):
        self.__inorder_helper(self.__root)
         
    def __inorder_helper(self, node):
        if node:
            self.__inorder_helper(node.left)
            print node.value
            self.__inorder_helper(node.right)
 
    def preorder(self):
        self.__preorderUtil(self.__root)
         
    def __preorderUtil(self, node):
        if node:
            print node.value
            self.__preorderUtil(node.left)
            self.__preorderUtil(node.right)
 
    def postorder(self):
        self.__postorderUtil(self.__root)
         
    def __postorderUtil(self, node):
        if node:
            self.__postorderUtil(node.left)
            self.__postorderUtil(node.right)
            print node.value
 
def buildExpressionTree(infix):
    postfix = postfixConvert(infix)
 
    stack = []
 
    for char in postfix:
        if char not in operatorPrecedence:
            node = Node(char)   
            stack.append(node)
        else:
            node = Node(char)
            right = stack.pop()
            left = stack.pop()
            node.right = right
            node.left = left
            stack.append(node)
     
    return ExressionTree(stack.pop())
 
print "In Order:"
buildExpressionTree("(5+3)*6").inorder()
print "Post Order:"
buildExpressionTree("(5+3)*6").postorder()
print "Pre Order:"
buildExpressionTree("(5+3)*6").preorder()
