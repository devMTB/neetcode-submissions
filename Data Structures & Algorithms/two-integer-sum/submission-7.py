class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countMap = {}
        index = 0
        for num in nums:
            equals = target - num
            if num not in countMap:
                countMap[num] = index
                print(index)
                index += 1
            else:
                if nums[index] >= countMap[num]:
                    return [countMap[num], index]
        index = 0
        for num in nums:
            equals = target - num
            print(equals)
            print(index)
            print("here")
            if equals in countMap and countMap[equals] != index:
                if countMap[equals] >= countMap[num]:
                    return [countMap[num], countMap[equals]]
                else:
                    return [countMap[equals], countMap[num]]
            index += 1

