class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueLocationHash = {}
        for i, currentValue in enumerate(nums):
            expectedValue = target - currentValue
            if expectedValue in valueLocationHash:
                expectedValueLocation = valueLocationHash[expectedValue]
                return  [i, expectedValueLocation] if i < expectedValueLocation else [expectedValueLocation, i]
            else:
                valueLocationHash[currentValue] = i
        return []
