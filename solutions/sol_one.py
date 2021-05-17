class Solution:
	def setKthBit(self, N, K):
        return((1 << K) | N) # it will shift 1 to the left k times of the number and then it will perform or operation
