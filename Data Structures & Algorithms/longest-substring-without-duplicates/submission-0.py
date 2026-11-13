class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        l, r = 0, 0
        len_s = len(s)
        max = 0
        while (r < len_s):
            while s[r] in unique:
                unique.pop(s[l], None)
                l = l + 1
            unique[s[r]] = 1
            max = (r - l + 1) if max < (r - l + 1) else max
            r = r + 1

        return max
            


