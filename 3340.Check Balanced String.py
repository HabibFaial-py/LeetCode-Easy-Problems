class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        total1 = 0
        total2 = 0
        for i in range(len(num)):
            if i % 2 == 0:
                total1 = total1 + int(num[i])
            else:
                total2 = total2 + int(num[i])
        if total1 == total2:
            return True
        else:
            return False
