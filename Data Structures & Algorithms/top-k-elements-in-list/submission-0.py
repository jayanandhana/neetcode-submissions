class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        for number in nums:
            countMap[number] += 1
        sortedCount = sorted(countMap.values(), reverse = True)
        slicedSortedCount = sortedCount[0:k]
        output = []
        for number, count in countMap.items():
            if count in slicedSortedCount:
                output.append(number)
        return output


