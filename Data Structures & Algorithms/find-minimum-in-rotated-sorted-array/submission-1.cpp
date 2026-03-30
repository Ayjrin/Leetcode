class Solution {
public:
    int findMin(vector<int> &nums) {
        int left = 0;
        int right = 0;
        int target = 0;
        int maxLength = nums.size();
        int i = 0;
        int min = nums[0];

        for (int i = 0; i < maxLength; i++){
            if (nums[i] < min){
                min = nums[i];
            }
        }

        return min;
    }
};
