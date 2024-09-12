class Solution:
    def climbStairs(self, n: int) -> int:
        fib = []
        if n == 0:
            return 0
        
        fib.append(0)
        fib.append(1)

        for i in range(n):
            fib.append(fib[i] + fib[i+1])

        return fib[n+1]