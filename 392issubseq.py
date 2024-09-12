class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it1=0
        it2=0

        while it2 != len(t):
            if it1 == len(s):
                return True

            if s[it1] == t[it2]:
                it1 += 1
                it2 += 1
            else:
                it2 += 1

        if it1 == len(s): return True
        else: return False