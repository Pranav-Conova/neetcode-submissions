class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        result_list = {}
        used = []
        for str in strs:
            char_map = {}
            for char in str:
                char_map[char] = char_map.get(char, 0) + 1
            if str_map: 
                g = 0
                for key, value in str_map.items():
                    if value == char_map:
                        f_list = result_list.get(key, [key])
                        f_list.append(str)
                        used.extend(f_list)
                        result_list[key] = f_list
                        g = 1
                if g == 0:
                     str_map[str] = char_map
            else:
                str_map[str] = char_map
            result = list(result_list.values())
            result.extend([[str] for str in strs if str not in used])
        return result
