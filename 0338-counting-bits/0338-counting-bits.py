# class Solution:
#     def countBits(self, n: int) -> List[int]:
        
#         def numBits(n: int) -> int:
#             sum = 0
#             while n != 0:
#                 sum += 1
#                 n &= (n-1)
#             return sum
    
#         ans = [0] * (n + 1)
#         for x in range(n + 1):
#             ans[x] = numBits(x)
            
#         return ans
    
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1,n + 1):
            ans[x] = ans[x & (x - 1)] + 1
            
        return ans
        
        
    

        