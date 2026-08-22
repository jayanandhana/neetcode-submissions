
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramHelperMap = {}
        anagramSets = []
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in anagramHelperMap:
                indexToInsert = anagramHelperMap[sortedWord]
                anagramSets[indexToInsert].append(word)
            else:
                anagramHelperMap[sortedWord] = len(anagramSets)
                anagramSets.append([word]) 
        return anagramSets