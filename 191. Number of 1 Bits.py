class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        binary_num = bin(n)
        newstring = str((binary_num)[2:])
        for i in range(len(newstring)):
            if newstring[i] == '1':
                count += 1
        return count
