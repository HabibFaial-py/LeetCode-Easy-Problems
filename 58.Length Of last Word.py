class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == ' ' and length > 0:
                break
            if char != ' ':
                length += 1

        return length