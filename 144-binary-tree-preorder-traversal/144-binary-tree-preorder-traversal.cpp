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
    void preOrder(TreeNode *root,vector <int> &res){
        if(root!=NULL){
            res.push_back(root->val);
            preOrder(root->left,res);
            preOrder(root->right,res);
        }
    }
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector <int> res;
        if(root == nullptr)
            return res;
        preOrder(root,res);
        return res;
    }
};