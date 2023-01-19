/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let leftSum = 0;
    let sum = 0;
    for(let num of nums){
        sum += num;
    }
    
    let rightSum = sum;
    for(let i = 0; i < nums.length; i++){
        rightSum = rightSum - nums[i];
        
        if(rightSum === leftSum) return i;
        
        leftSum += nums[i];
    }
    return -1;
};