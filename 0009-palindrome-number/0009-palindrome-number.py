class Solution:
    def isPalindrome(self, x: int) -> bool:    # O(log10 (n)). We divided the input by 10 for every iteration. | O(1) space

        # Special cases:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_num = 0
        while(x > reverted_num):
            reverted_num = reverted_num * 10 + x % 10
            x //= 10
            
        # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
            
        return x == reverted_num or x == reverted_num // 10
        
        
#       def isPalindrome(self, x: int) -> bool:  # O(N) time | O(N) space N: # of digits
#             if x < 0:
#                 return False

#             numbers = []
#             while x > 9:
#                 numbers.append(x % 10)
#                 x = x // 10
#             numbers.append(x)

#             return numbers == numbers[::-1] # O(N) time to reverse the array