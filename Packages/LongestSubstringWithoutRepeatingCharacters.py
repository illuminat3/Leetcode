class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        startPointer = 0
        length = 0

        for endPointer in range(0, len(s)):
            while s[endPointer] in charSet:
                charSet.remove(s[startPointer])
                startPointer += 1
            charSet.add(s[endPointer])
            length = max(length, endPointer - startPointer + 1)
        
        return length