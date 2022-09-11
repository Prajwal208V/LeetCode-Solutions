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
    vector<vector<int>> result;
    private:
      void pathSum(TreeNode *root,int targetSum,vector<int>tempArr,int sum){
          if(!root)
              return ;
          sum+=root->val;
          tempArr.push_back(root->val);
          if(sum==targetSum && !root->left && !root->right)
             result.push_back(tempArr);
          pathSum(root->left,targetSum,tempArr,sum);
          pathSum(root->right,targetSum,tempArr,sum);
      }
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> tempArr;
        pathSum(root,targetSum,tempArr,0);
        return result;
    }
};