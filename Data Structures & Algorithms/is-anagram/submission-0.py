class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = "".join(sorted(s))
        sort_t = "".join(sorted(t))

        if len(sort_s) != len(sort_t):
            return False

        for i in range(len(sort_s)):
            if sort_s[i] == sort_t[i]:
                continue
            else:
                return False

        return True