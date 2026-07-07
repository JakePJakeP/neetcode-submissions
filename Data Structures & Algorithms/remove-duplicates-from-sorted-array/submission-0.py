class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        k = 0
        while k < len(nums):
            if nums[k] not in seen:
                seen.add(nums[k])
                k += 1
            else:
                nums.pop(k)
        return k
        