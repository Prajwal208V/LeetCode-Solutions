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
public:
    int result=INT_MAX;
    int last=INT_MIN;
    void inorderTravesl(TreeNode *root){
        if(!root)
            return;
        inorderTravesl(root->left);
        if(last==INT_MIN)
            last=root->val;
        else{
            result=min(abs(root->val-last),result);
            last=root->val;
        }
        inorderTravesl(root->right);
        
    }
    int getMinimumDifference(TreeNode* root) {
        inorderTravesl(root);
        return result;
    }
};