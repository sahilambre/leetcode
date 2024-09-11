class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)

            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False

    
    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digits = n % 10
            digits = digits ** 2
            output += digits
            n = n // 10
        return output 