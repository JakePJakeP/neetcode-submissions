class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writeIndex = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[writeIndex] = nums[i]
                writeIndex += 1
        return writeIndex
        