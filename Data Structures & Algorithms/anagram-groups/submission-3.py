class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        result_list = {}
        for str in strs:
            char_map = {}
            for char in str:
                char_map[char] = char_map.get(char, 0) + 1
            if str_map: 
                return list(list(str_map))
                for key, value in str_map:
                    if value == char_map:
                        result_list[str] = result_list.get(key, [key]).append(str)
            else:    
                str_map[str] = char_map

        return list(result_list.values())
