# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        returnList = [root.val]
        returnList += self.preorderTraversal(root.left)
        returnList += self.preorderTraversal(root.right)
        
        return returnList

        
        
        

        