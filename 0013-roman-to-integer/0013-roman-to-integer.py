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
        roman_numerals = [*s]
        sum_integer = 0
        prev_value = 0
        for i in range(len(roman_numerals)-1, -1, -1):
            roman_numeral = roman_numerals[i]
            numeral_value = values[roman_numeral]
            
            if numeral_value < prev_value:
                sum_integer -= numeral_value
            else:
                sum_integer += numeral_value
                
            prev_value = numeral_value
            
        return sum_integer
                
                
            
        