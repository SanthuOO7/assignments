class Solution:
    def longestCommonSum(self, arr1, arr2, n): 
        # code here 
        maxlen = 0
        diff = {}
        sum1 = 0
        sum2 = 0
        for i in range(n):
            sum1 +=arr1[i]
            sum2 += arr2[i]
    
            difflen = sum1 - sum2
    
            if difflen == 0:
                maxlen = i + 1
    
            elif difflen not in diff:
                diff[difflen] = i
            else:
                length = i - diff[difflen]
                maxlen = max(length, maxlen)
    
        return maxlen