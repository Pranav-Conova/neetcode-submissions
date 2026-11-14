class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        seen = []
        last_num = n
        while sum != 1 or sum not in seen:
            sum = 0
            digit = last_num
            while digit:
                sum = ((digit %10)^2) + sum
                digit = digit //2
            else:
                last_num = sum
                seen.append(sum)
 
            if sum == 1:
                return True
            else:
                return False