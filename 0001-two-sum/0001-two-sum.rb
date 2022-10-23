# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}

#O(N2) time | O(1) space
# def two_sum(nums, target)
#     (0...nums.length).each do |i|
#        (0...nums.length).each do |j|
#             if j > i && nums[i] + nums[j] == target
#                 return [i,j] 
#             end
#        end
#     end
# end

#O(N) Time | O(n) space
def two_sum(nums,target)
    hash = {}
    nums.each_with_index do |num,i|
        diff = target - num
        if hash[diff].nil?
            hash[num] = i
        else
            return [hash[diff],i] 
        end
    end
end

#O(nlogn) time | O(1)space
# def two_sum(nums,target)
#     sorted = nums.sort
#     left = 0
#     right = nums.length - 1
#     while left < right
#         sum = sorted[left] + sorted[right]
#         if target == sum
#            return [left,right] 
#         elsif target < sum
#             right -= 1
#         elsif target > sum
#             left += 1
#         end
#     end
# end


