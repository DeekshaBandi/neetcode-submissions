class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = {}
        for i in s1:
            s1Count[i] = 1 + s1Count.get(i, 0)
        
        s2Count = {}
        for j in range(len(s1)):
            c = s2[j]
            s2Count[c] = 1 + s2Count.get(c, 0)

        if s1Count == s2Count:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            # add the new character entering the window
            c = s2[right]
            s2Count[c] = 1 + s2Count.get(c, 0)

            # remove the character leaving the window
            leftChar = s2[left]
            s2Count[leftChar] -= 1
            if s2Count[leftChar] == 0:
                del s2Count[leftChar]
            left += 1

            if s1Count == s2Count:
                return True

        return False