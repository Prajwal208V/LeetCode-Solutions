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
    void treePath(TreeNode *root,vector<string> &res,string curStr){
        if(!root)
            return;
        if(!root->left && !root->right){
            curStr+=to_string(root->val);
            res.push_back(curStr);
            return ;
        }
        curStr+=to_string(root->val)+"->";
        treePath(root->left,res,curStr);
        treePath(root->right,res,curStr);
    }
public:
    vector<string> binaryTreePaths(TreeNode* root) {
      vector <string> res;
      string curStr="";
      treePath(root,res,curStr);
      return res;
    }
};