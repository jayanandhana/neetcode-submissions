class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        letterCountHash = {'s': {}, 't': {}};
        for i in range(len(s)):
            letterCountHash['s'][s[i]] = letterCountHash['s'].get(s[i], 0) + 1;
            letterCountHash['t'][t[i]] = letterCountHash['t'].get(t[i], 0) + 1;
        
        return letterCountHash['s'] == letterCountHash['t'];