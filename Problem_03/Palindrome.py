class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        reverse = 0
        if(x<0):
            return False
        while(x>0):
            last_digit = x%10
            reverse = reverse *10 +last_digit
            x = x//10
        if(reverse==number):
            return True
        else:
            return False