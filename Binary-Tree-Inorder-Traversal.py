# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        returnList = []
        returnList += self.inorderTraversal(root.left)
        returnList.append(root.val)
        returnList += self.inorderTraversal(root.right)
        
        return returnList