class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    if first < 0 or second < 0:
                        stack.append(math.ceil(first / second))
                    else:
                        stack.append(math.floor(first / second)) 
            else:
                stack.append(int(token))
        return stack[0]
10 -22