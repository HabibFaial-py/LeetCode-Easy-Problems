class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        newa = int(a, 2)
        newb = int(b, 2)
        total = newa + newb
        binary_rep = bin(total)[2:]
        return binary_rep
