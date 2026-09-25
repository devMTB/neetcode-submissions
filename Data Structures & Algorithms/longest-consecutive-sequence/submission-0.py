class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        start = 0
        ctr = 0
        nextN = 0
        longS = 0

        for n in nums:
            if (n - 1) not in nset:
                nextN = n
                ctr = 1
                while (nextN + 1) in nset:
                    nextN = nextN + 1
                    ctr += 1
                if (longS < ctr):
                    longS = ctr
                
        return longS