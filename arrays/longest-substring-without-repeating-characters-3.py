class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, m, result = 0, {}, 0

        for j in range(len(s)):
            if(s[j] in m):
                i = max(i, m[s[j]])

            result = max(result, j - i + 1)
            m[s[j]] = j + 1

        return result
