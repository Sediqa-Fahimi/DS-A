class Solution:
    def isValid(self, s: str) -> bool:
        validCodes = [(40,41), (91, 93), (123, 125)]
        stack = []
        for char in s:
            charCode = ord(char)
            if charCode == 40 or charCode == 91 or charCode == 123:
                stack.append(charCode)
            else:
                if not stack:
                    return False
                
                recentChar = stack.pop()
                if (recentChar, charCode) not in validCodes:
                    return False
                
        return len(stack) == 0
        
  
        