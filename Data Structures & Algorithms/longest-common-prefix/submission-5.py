class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        longestPrefix = strs[0]

        for i in range(1, len(strs)):
            minLen = min(len(longestPrefix), len(strs[i]))
            
            matchIndex = 0
            while matchIndex < minLen and longestPrefix[matchIndex] == strs[i][matchIndex]:
                matchIndex += 1
            
            longestPrefix = longestPrefix[:matchIndex]

            if not longestPrefix:
                return ""
        
        return longestPrefix
        
        