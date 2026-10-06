class Solution:
    def isPalindrome(self, s: str) -> bool:
        startPointer = 0
        endPointer = len(s) - 1
        isPalindromeFlag = True
        while startPointer < endPointer:
            if not s[startPointer].isalnum():
                startPointer = startPointer + 1
                continue
            if not s[endPointer].isalnum():
                endPointer = endPointer - 1
                continue
            print(s[startPointer], s[endPointer], s[startPointer] != s[endPointer])
            if s[startPointer].lower() != s[endPointer].lower():
                print('failure condition', s[startPointer], s[endPointer])
                isPalindromeFlag = False
                break
            startPointer = startPointer + 1
            endPointer = endPointer - 1
        return isPalindromeFlag