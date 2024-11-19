class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        newstring = ""
        result = []
        for i in range(len(digits)):
            newstring += str(digits[i])
        final = int(newstring) + 1
        for j in str(final):
            result.append(int(j))
        return result



