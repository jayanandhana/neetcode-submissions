class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valueOccurrenceMap = {};
        hasDuplicateNumber = False
        i = 0;
        while i < len(nums):
            value = nums[i];
            if valueOccurrenceMap.get(value, 0) == 1:
                hasDuplicateNumber = True;
                break;
            else:
                valueOccurrenceMap[value] = 1;
            i += 1;
        return hasDuplicateNumber;
        