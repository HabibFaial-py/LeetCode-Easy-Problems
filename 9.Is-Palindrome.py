class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        newstring = ""
        newx = str(x)

        for i in range(len(newx) - 1, -1, -1):
            newstring = newstring + newx[i]

        if newstring == newx:
            return True
        return False  
