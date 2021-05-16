class Solution:
	def setBits(self, n):
		# code here
		n = str(bin(n))
# 		print(n)
        one_count = 0
        for i in n:
            if i == "1":
                one_count+=1
        return one_count