class Solution {
    public int removeDuplicates(int[] nums) {
        int n, i = 0, j;
        n = nums.length;
        for(j=1;j<n;j++)
        {
            if(nums[i]!=nums[j])
            {
                i++;
                nums[i] = nums[j];
            }
        }
        return i+1;
        
    }
}