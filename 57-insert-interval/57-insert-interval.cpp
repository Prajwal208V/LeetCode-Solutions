class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        intervals.push_back(newInterval);
        sort(intervals.begin(),intervals.end());
        vector<int> temp_vect=intervals[0];
        vector<vector<int>> result_vect;
        for(auto itr:intervals){
            if(itr[0]<=temp_vect[1])
                temp_vect[1]=max(itr[1],temp_vect[1]);
            else{
                result_vect.push_back(temp_vect);
                temp_vect=itr;
            }
        }
        result_vect.push_back(temp_vect);
        return result_vect;
    }
};