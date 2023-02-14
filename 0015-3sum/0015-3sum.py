class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        i = 0
        curr_sum = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                break
                
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
                while i + 1 != left and nums[left] == nums[left-1] and left < right:
                    left += 1
                while right < len(nums) - 2 and nums[right] == nums[right+1] and left < right:
                    right -= 1
                    
                curr_sum = 0
            i += 1
        
        return results
   