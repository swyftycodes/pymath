def find_within_brackets(array):
    stack = []
    values = []
    for char in array:
        if char == "[":
            stack.append(values)
            values = []
        elif char == "]":
            if len(stack) > 0:
                prev_values = stack.pop()
                prev_values.append(values)
                values = prev_values
            else:
                raise ValueError("Unbalanced brackets")
        else:
            values.append(char)
    if len(stack) > 0:
        raise ValueError("Unbalanced brackets")
    return values

def stringerize(array):
    stack = []

    for item in array:
        if str(item).endswith('.0'):
            item = int(item)
        if type(item) == list:
            stack.append('[')
            stack.append(stringerize(item))
            stack.append(']')
        else:
            stack.append(str(item))

    return ' '.join(stack)

def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
