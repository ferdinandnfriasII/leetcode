#leetcode practice question 226
#Given the root of a binary tree, invert the tree and return the root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 0
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root