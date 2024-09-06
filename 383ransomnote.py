class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = dict()

        for letter in magazine:
            if letter in map:
                map[letter] += 1
            else:
                map[letter] = 1
        
        for letter in ransomNote:
            if letter in map:
                if map[letter]>0:
                    map[letter] -= 1
                else:
                    return False
            else:
                return False
        
        return True
