class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = []
        if len(s) == 0: 
            return 0
        
        max_num = 1      
        for i in range(len(s)-1): 
            nums = 1
            char = []
            char.append(s[i])
            for j in range(i+1, len(s)):  
                if s[j] != s[i] and s[j] not in char:
                    char.append(s[j])
                    nums += 1
                    max_num = max(max_num, nums)
                else:
                    break
        
        return max_num