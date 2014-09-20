# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result = []
        if not root:
            return result
        
        self.do(root, result)
        return result
        
    def do(self, node, result):
        if node.left:
            self.do(node.left, result)
        if node.right:
            self.do(node.right, result)
        result.append(node.val)
        return