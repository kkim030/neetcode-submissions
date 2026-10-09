class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for string in s:
            if ('(' == string or '{' == string or '[' == string):
                stack.append(string)
            else:
                if len(stack) > 0:
                    top = stack[-1]
                    if ((string == ')' and top == '(') or 
                    (string == '}' and top == '{') or
                    (string == ']' and top == '[')):
                        stack.pop()
                    else: 
                        return False
                else:
                    stack.append(string)
                    
        return len(stack) == 0
        
        