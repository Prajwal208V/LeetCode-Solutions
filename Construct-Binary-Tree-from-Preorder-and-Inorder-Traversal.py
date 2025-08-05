# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idex = 0
        
        def helper(left:int, right:int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            root_val = preorder[self.pre_idex]
            self.pre_idex += 1
            root = TreeNode(root_val)
            
            index = inorder_index[root_val] 
            
            root.left = helper(left, index-1)
            root.right = helper(index+1, right)
            
            return root
        return helper(0, len(inorder)-1)
        