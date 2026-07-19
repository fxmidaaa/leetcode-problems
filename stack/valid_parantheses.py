class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for char in s:
            if char in mapping:
                stack.append(mapping[char])
            else:
                if not stack or stack.pop() != char:
                    return False
                   
        return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            match char:
                case '(' | '{' | '[':
                    stack.append(char)
                    
                case ')':
                    if not stack or stack.pop() != '(':
                        return False
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
                case ']':
                    if not stack or stack.pop() != '[':
                        return False
                        
        return len(stack) == 0
