class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0) or (x % 10 == 0 and x != 0):
            return False
        arr = [int(n) for n in str(x)]
        j=len(arr)-1
        for i in range (len(arr)):
            if arr[i] != arr[j]:
                return False
            if i == j:
                break
            j-=1
        return True

##super fast version
# class Solution:
# def isPalindrome(self, x: int) -> bool:
# return str(x) == str(x)[::-1]
