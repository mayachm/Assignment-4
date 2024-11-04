def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

print(is_balanced("(1+2)-3*[41+6]")) 
print(is_balanced("(1+2)-3*[41+6}")) 
print(is_balanced("(1+2)-3*[41+6"))   
print(is_balanced("(1+2)-3*]41+6["))  
print(is_balanced("(1+[2-3]*4{41+6})"))  