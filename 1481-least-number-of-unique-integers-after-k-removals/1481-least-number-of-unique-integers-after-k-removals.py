import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # hp = list(collections.Counter(arr).values())
        # heapq.heapify(hp)
        # while k > 0:
        #     k -= heapq.heappop(hp)
        # return len(hp) + (k < 0)  
        counter = {}
        for num in arr:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
                
        hp = list(counter.values())
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)
            
        return len(hp) + (k < 0)
        