class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        string = bin(n)[2:]
        string = string.zfill(32)
        newstring = ""
        for i in range(len(string) - 1, -1, -1):
            newstring += string[i]
        return int(newstring, 2)


