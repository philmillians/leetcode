class Solution:
    def fib(self, n: int) -> int:
        length_arr = n
        fibNumbers=[0,1]
        if n ==0:
            return 0
        elif n==1:
            return 1
        for i in range(2,length_arr+1):
            fibNumbers.append(fibNumbers[i-1]+fibNumbers[i-2])
        return fibNumbers[n]
    
