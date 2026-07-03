class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqDict = dict()
        for num in nums:
            if num not in freqDict:
                freqDict[num] = 1
            else:
                freqDict[num] += 1
        maxFreq = 0
        maxNum = 0
        for key in freqDict:
            if freqDict[key] > maxFreq:
                maxFreq = freqDict[key]
                maxNum = key
        return maxNum
        