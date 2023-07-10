from utils import isfloat, find_within_brackets

def tokenize_float(string):
    string = string.replace(' ', '')

    stack = []
    ops = ['+', '-', '*', '/', '^', '[', ']']

    temp = ''

    for i, char in enumerate(string):
        if isfloat(char) or char == '.':
            temp += char
        elif char in ops:
            if not temp == '':
                stack.append(float(temp))
                temp = ''
            if char == '-' and string[i - 1] in ops or char == '-' and i == 0:
                temp += char
            else:
                stack.append(char)
        
        #if end of string append temp
        if i + 1 == len(string) and not temp == '':
            stack.append(float(temp))
            temp = ''

    return find_within_brackets(stack)
