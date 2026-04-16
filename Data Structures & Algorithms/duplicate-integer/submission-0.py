class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        isDup = False
        for num in nums:
            # If countMap does not contain name
            if num not in countMap:
                countMap[num] = 1
            else:
                countMap[num] += 1
            if countMap[num] >= 2:
                isDup = True
        return isDup