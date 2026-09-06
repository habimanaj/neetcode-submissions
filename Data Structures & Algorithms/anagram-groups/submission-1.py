class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1

            keyTup = tuple(count)
            if keyTup in res:
                res[keyTup].append(s)
            else:
                res[keyTup] = [s]
        
        resList = []
        for s in res:
            resList.append(res[s])
        return resList