/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) { // O(N) time | O(1) space
	let max = 0
	let currentMax, distance;
	let start = 0;
	let end = height.length - 1;
	while(start < end){
		distance = end - start;
		currentMax = distance * Math.min(height[start],height[end]);
		if(currentMax > max) max = currentMax;
		if(height[start] > height[end]){
			end--;
		}else{
			start++;
		}
	}
	return max;
};