class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return(False)
        num=0
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        return(str(x) == str(x)[::-1])
        