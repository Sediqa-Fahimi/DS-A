/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
// O(log n) time | O(1) space
var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    
    while(left <= right){
        let mid = Math.floor((left + right) / 2);
        
        if(nums[mid] === target) return mid;
        
        if(target > nums[mid]){
            left = mid + 1;
        }else{
            right = mid - 1;
        }
    }
    return -1;
};