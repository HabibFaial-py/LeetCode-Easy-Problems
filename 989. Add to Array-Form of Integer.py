class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        newstring = ""
        result = []
        for i in range(len(num)):
            newstring += str(num[i])
        final = int(newstring) + k
        for j in str(final):
            result.append(int(j))
        return result
