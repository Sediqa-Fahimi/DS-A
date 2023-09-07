/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    const n = digits.length;
    for(let i = n - 1; i >= 0; i--){
        if(digits[i] === 9){
            digits[i] = 0;
        }else{
            digits[i] += 1;
            return digits;
        }
    }
    digits = new Array(n + 1).fill(0);
    digits[0] = 1;
    return digits;
};