# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
import heapq as hq

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def countOnes(n):
            cnt = 0
            while n:
                n = n & n-1
                cnt += 1

            return cnt

        tmp = []        
        for n in arr:
            ones = countOnes(n)
            tmp.append((ones, n))

        hq.heapify(tmp)
        res = []

        while tmp:
            res.append(hq.heappop(tmp)[1])

        return res
