class Solution(object):
    def isPalindrome(self, x):
        temp = x
        rev = 0
        if temp > 0:
            for i in range(1, len(str(temp)) + 1):
                digit = x % 10
                rev = rev * 10 + digit
                x = x // 10
        else: 
            print("False Enter Positive Number")

        if rev == temp:        
            return True
        else:
            return False
        