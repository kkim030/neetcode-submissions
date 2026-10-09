class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = sorted(s)
        t_array = sorted(t)

        return s_array == t_array
        