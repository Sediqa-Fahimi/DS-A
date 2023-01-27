class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counter = {}
        for char in s:
            if char not in counter: counter[char] = 0
            counter[char] += 1
        for char in t:
            if char not in counter: return False
            elif counter[char] == 0: return False
            counter[char] -= 1
            
        return True