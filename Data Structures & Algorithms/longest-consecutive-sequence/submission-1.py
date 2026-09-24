class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        locationHash = dict()
        for index, number in enumerate(nums):
            locationHash[number] = index

        longestCount = 0
        currentCount = 1
        for number in sorted(locationHash.keys()):
            nextNumber = number + 1
            if nextNumber in locationHash:
                currentCount = currentCount + 1
            else:
                longestCount = currentCount if currentCount > longestCount else longestCount
                currentCount = 1
        return longestCount
