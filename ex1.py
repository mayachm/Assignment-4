from collections import deque

def is_palindrome(input_string):
    input_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    stack = []
    queue = deque()
    
    for char in input_string:
        stack.append(char)
        queue.append(char)
    
    while stack:
        if stack.pop() != queue.popleft():
            return False
    
    return True

print(is_palindrome("mom"))  
print(is_palindrome("Neveroddoreven")) 
print(is_palindrome("hello"))  