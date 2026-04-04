class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                if top == '(' and ch != ')':
                    return False
                elif top == '[' and ch != ']':
                    return False
                elif top == '{' and ch != '}':
                    return False

        return len(stack) == 0 