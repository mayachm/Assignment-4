def decode_message(message):
    stack = []
    
    for char in message:
        if char == '*':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    
    decoded_message = ''.join(stack)
    return decoded_message[::-1] 

input_message = "SIVLE ****** DAED TNSI ***"
output_message = decode_message(input_message)
print(output_message)