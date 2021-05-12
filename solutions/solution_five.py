class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n, s, d, k = len(A), 0, defaultdict(lambda: 0), 0
        d[0] = 1
        for x in A:
          s += x
          s %= K
          k += d[s]
          d[s] += 1
        return k