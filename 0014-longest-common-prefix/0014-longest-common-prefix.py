class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if((i < len(strs[j]) and strs[j][i] != char) or i >= len(strs[j])):
                    return str
            
            str += strs[0][i]
         
        return str