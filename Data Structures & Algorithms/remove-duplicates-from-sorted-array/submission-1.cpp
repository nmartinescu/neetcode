class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left = 1;
        for (int right = 1; right < nums.size(); right++) {
            int prev = nums[right - 1];
            if (nums[right] != prev) {
                nums[left++] = nums[right];
            } 

        }

        return left;
    }
};