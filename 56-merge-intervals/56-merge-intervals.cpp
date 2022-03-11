class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
       sort(intervals.begin(),intervals.end());
        vector<int> temp_vect=intervals[0];
        vector<vector <int>> result_vect;
        for(auto itr:intervals){
            if(itr[0]<=temp_vect[1])
                temp_vect[1]=max(temp_vect[1],itr[1]);
            else{
                result_vect.push_back(temp_vect);
                temp_vect=itr;
            }
        }
        result_vect.push_back(temp_vect);
        return result_vect;
    }
};