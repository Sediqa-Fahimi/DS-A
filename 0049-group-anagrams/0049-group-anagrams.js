/**
 * @param {string[]} strs
 * @return {string[][]}
 */

// O(N * K) time | O(N * K) space
var groupAnagrams = function(strs){
    const anagrams = {};
    const count = new Array(26);
    
    for(let str of strs){ 
        count.fill(0);
        let strArr = str.split("");
        for(let char of strArr){ 
            count[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
        }
        
        let keyArr = [];
        for(i = 0; i < 26; i++){
            keyArr.push("#");
            keyArr.push(count[i]);
        }
        let keyStr = keyArr.join("");
        
        if(!anagrams[keyStr]) anagrams[keyStr] = [str];
        else anagrams[keyStr].push(str);
        
    }
    return Object.values(anagrams);
}

// O(N * KlogK) time | O(NK) space
// var groupAnagrams = function(strs) {
//     const anagrams = {};
//     for(let str of strs){ 
//         let sorted = str.split("").sort().join("");
//         anagrams[sorted] ? anagrams[sorted].push(str) : anagrams[sorted] = [str];
//     }
//     return Object.values(anagrams);
// };

