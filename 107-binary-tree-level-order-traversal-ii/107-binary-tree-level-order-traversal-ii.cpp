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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result;
        if(root==NULL)
            return result;
        queue<TreeNode *>que;
        que.push(root);
        while(!que.empty()){
            int siz=que.size();
            vector<int> level;
            for(int i=0;i<siz;i++){
                TreeNode* levelnode=que.front();
                que.pop();
                level.push_back(levelnode->val);
                if(levelnode->left!=NULL)
                    que.push(levelnode->left);
                if(levelnode->right!=NULL)
                    que.push(levelnode->right);
            }
            result.push_back(level);
        }
        reverse(result.begin(),result.end());
        return result;
    }
};