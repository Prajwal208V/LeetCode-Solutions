/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private :
    int res=0;
    int maxDepthFun(TreeNode *root){
        if(!root)
            return 0;
        int leftSubTreeLen=maxDepthFun(root->left);
        int rightSubTreeLen=maxDepthFun(root->right);
        res=max(leftSubTreeLen+rightSubTreeLen,res);
        cout<<res<<" ";
        return max(leftSubTreeLen,rightSubTreeLen)+1;
    }
    
public:
    int diameterOfBinaryTree(TreeNode* root) {
        maxDepthFun(root);
        return res;
    }
};