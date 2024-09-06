import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)

        n = len(s)
        i = 0

        for i in range(int(n/2)):
            if s[i] != s[n-i-1]: 
                return False

        return True