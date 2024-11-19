class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newlist = []
        for i in range(len(nums)):
            if nums[i] not in newlist:
                if nums.count(nums[i]) > 1:
                    newlist.append(nums[i])
        return newlist
