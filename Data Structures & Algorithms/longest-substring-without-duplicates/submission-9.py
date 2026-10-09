class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = set()
        maximum = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in record:
                record.add(s[j])
                j += 1
                maximum = max(j - i, maximum)
            else:
                record.remove(s[i])
                i += 1
        return maximum