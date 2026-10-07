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
                res_char = result_list.pop() if result_list else ""
                if res_char != pair:
                    return False
        if not result_list:
            return True
        else:
            return False
                    

                
            
