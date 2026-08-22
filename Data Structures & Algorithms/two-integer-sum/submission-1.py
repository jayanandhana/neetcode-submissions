class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueLocationHash = {};
        for i in range(len(nums)):
            currentValue = nums[i];
            expectedValue = target - currentValue;
            if expectedValue in valueLocationHash:
                expectedValueLocation = valueLocationHash[expectedValue];
                return  [i, expectedValueLocation] if i < expectedValueLocation else [expectedValueLocation, i];
            else:
                valueLocationHash[currentValue] = i;
        return [];


# first solution, doesn't handle duplicates, can be done in a single pass as well
    # class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     valueLocationHash = {};
    #     for i in range(len(nums)):
    #         num = nums[i];
    #         if valueLocationHash.get(num):
    #             continue;
    #         else:
    #             valueLocationHash[num] = i;
    #     for i in range(int(len(nums) / 2) + 1):
    #         currentValue = nums[i];
    #         expectedValue = target - currentValue;
    #         if valueLocationHash.get(expectedValue, False):
    #             return [valueLocationHash[currentValue], valueLocationHash[expectedValue]];
    #     return False;