class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arr =nums
        n = len(arr)
        res = 0

        # Calculate all subarrays
        for i in range(n):
            summ = 0           
            for j in range(i, n):

                # Calculate required sum
                summ += arr[j]

                # Check if sum is equal to
                # required sum
                if summ == k:
                    res += 1

        return res