class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_hash_map = {}
        for char in s:
            count = char_hash_map.get(char, 0)
            char_hash_map[char] = count +1
        for char in t:
            value = char_hash_map.get(char, 0)
            if not value :
                return False
            char_hash_map[char] = value - 1
        if sum(char_hash_map.values()) != 0:
            return False
        else: 
            return True
            
