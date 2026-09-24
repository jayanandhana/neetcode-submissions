class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixList = []
        sizeOfInput = len(nums)
        postfixList = [1] * sizeOfInput
        for index in range(sizeOfInput):
            prefixIndex = index
            postfixIndex = sizeOfInput - index - 1
            # prefix computation
            if prefixIndex - 1 < 0:
                prefixList.append(nums[prefixIndex])
            else:
                prefixList.append(prefixList[prefixIndex - 1] * nums[prefixIndex])
            # postfix computation 
            if postfixIndex >= sizeOfInput - 1:
                postfixList[postfixIndex] = nums[postfixIndex]
            else:
                postfixList[postfixIndex] = postfixList[postfixIndex + 1] * nums[postfixIndex]

        # output array computation
        outputList = []
        for index in range(sizeOfInput):
            prefixIndex = index - 1;
            postfixIndex = index + 1;
            prefixListValue = 1 if prefixIndex < 0 else prefixList[prefixIndex]
            postfixListValue = 1 if postfixIndex > sizeOfInput - 1 else postfixList[postfixIndex]
            outputList.append(prefixListValue * postfixListValue)
        return outputList