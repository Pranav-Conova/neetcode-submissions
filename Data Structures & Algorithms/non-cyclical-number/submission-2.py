class Solution:
    def sumSquare(self, n):
        sum =0
        while n:
            sum = sum + ((n%10)**2)
            n= n//10
        return sum
    def isHappy(self, n: int) -> bool:
        seen = []
        num = n
        while 1:
            a = self.sumSquare(num)
            if a == 1:
                return True
            elif a in seen:
                print(seen)
                return False
            seen.append(a)
            num = a
        