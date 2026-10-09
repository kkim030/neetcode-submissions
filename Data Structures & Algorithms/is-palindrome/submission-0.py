class Solution:
    def isPalindrome(self, s: str) -> bool:

        #lower the strings
        #erase the spaces 
        #ignore all non-alphanumeric 
        new = ""

        for char in s:
            if char.isalnum():
                new += char.lower()
        
        return new == new[::-1]




        