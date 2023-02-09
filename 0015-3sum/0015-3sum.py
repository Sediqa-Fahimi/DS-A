class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        curr = 0
        curr_sum = 0
        while curr < len(nums) - 2:
            left = curr + 1
            right = len(nums) - 1
            if curr > 0 and nums[curr] == nums[curr-1]:
                curr += 1
                continue
            while left < right:
                curr_sum = nums[curr] + nums[left] + nums[right]
                if curr_sum == 0:
                    results.append([nums[curr], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
                while curr + 1 != left and nums[left] == nums[left-1] and left < right:
                    left += 1
                while right < len(nums) - 2 and nums[right] == nums[right+1] and left < right:
                    right -= 1
                    
                curr_sum = 0
            curr += 1
        
        return results
   