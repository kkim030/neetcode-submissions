class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")":"(", "]":"[","}":"{"}
        stack = []

        for c in s:
            if c not in Map: 
                stack.append(c)
                continue
            elif not stack or Map[c] != stack[-1]:
                return False
            stack.pop()
        return not stack

        # for string in s:
        #     if ('(' == string or '{' == string or '[' == string):
        #         stack.append(string)
        #     else:
        #         if len(stack) > 0:
        #             top = stack[-1]
        #             if ((string == ')' and top == '(') or 
        #             (string == '}' and top == '{') or
        #             (string == ']' and top == '[')):
        #                 stack.pop()
        #             else: 
        #                 return False
        #         else:
        #             stack.append(string)
                    
        return not stack
        
        