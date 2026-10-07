class Solution:
    def isPalindrome(self, s: str) -> bool:
        straight_str = ((''.join(char for char in s if char.isalnum())).replace(" ", "")).lower()
        rev_str = straight_str[::-1]
        if straight_str == rev_str:
            return True
        return False