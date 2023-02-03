class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        romans = [*s]
        sum_int = 0
        prev_value = 0
        for i in range(len(romans)-1, -1, -1):
            roman = romans[i]
            roman_value = values[roman]
            
            if roman_value < prev_value:
                sum_int -= roman_value
            else:
                sum_int += roman_value
                
            prev_value = roman_value
            
        return sum_int
                
                
            
        