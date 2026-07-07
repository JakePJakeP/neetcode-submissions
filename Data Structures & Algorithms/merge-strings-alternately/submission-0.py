class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        smallerWordLen = min(len(word1), len(word2))
        if smallerWordLen == len(word1): largerWord = word2
        else: largerWord = word1
        i = 0
        while i < smallerWordLen:
            merged += word1[i]
            merged += word2[i]
            i += 1
        return merged + largerWord[smallerWordLen:]
