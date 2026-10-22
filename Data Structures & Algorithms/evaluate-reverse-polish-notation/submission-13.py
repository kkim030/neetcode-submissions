class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        numbers = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                numbers.append(int(t))
            else:
                a = numbers.pop() 
                b = numbers.pop()
                if "+" == t:
                    numbers.append(int(b + a))
                elif "-" == t:
                    numbers.append(b - a)
                elif "*" == t:
                    numbers.append(b * a)
                else:
                    numbers.append(int(b / a))
        return int(numbers.pop())