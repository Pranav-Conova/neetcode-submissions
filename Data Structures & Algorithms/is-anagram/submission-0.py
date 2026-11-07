class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = [char for char in s]
        for char in t:
            if char not in characters :
                return true
            characters.remove(char)
        if characters is not []:
            return true
        return false