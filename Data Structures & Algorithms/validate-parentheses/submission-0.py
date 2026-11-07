class Solution:
    def isValid(self, s: str) -> bool:
        result_list = []
        opened = ["[", "(", "{"]
        closed = ["]", ")", "}"]
        char_pair = {"]": "[", ")": "(", "}": "{"}
        for char in s :
            if char in opened:
                result_list.append(char)
            if char in closed:
                pair = char_pair[char]
                if result_list[-1] != pair:
                    return false
                else:
                    result_list.pop()
        if not result_list:
            return True
        else:
            return False
                    

                
            
