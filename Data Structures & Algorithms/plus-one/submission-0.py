class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reminder = 1
        new_list = []
        for num in digits[::-1]:
            new_digit = num + reminder
            if new_digit == 10:
                reminder = 1
                new_list = [0] + new_list
            else:
                reminder = 0
                new_list = [new_digit] + new_list
        if reminder:
            new_list = [reminder] + new_list
        return new_list


 