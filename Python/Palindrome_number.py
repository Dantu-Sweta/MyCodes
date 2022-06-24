class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def reverse(n):
            rev = 0
            while(n>0):
                rem = n%10
                rev = rev*10 + rem
                n = n//10
            return rev
        rev = reverse(x)
        if x == rev:
            return True
        else:
            return False