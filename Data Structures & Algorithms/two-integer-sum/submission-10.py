##################################

#Cleaner version of mine

###################################



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countMap = {}
        
        for index, num in enumerate(nums):
            equals = target - num
            
            # check first (this is the key fix)
            if equals in countMap:
                return [countMap[equals], index]
            
            # then store
            countMap[num] = index