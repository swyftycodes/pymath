def calc_float(expr_arr):
    # make things within brackets it's own array
    res = expr_arr 

    for i, item in enumerate(res):
        if type(item) == list:
            res[i] = calc_float(item)

            if len(res[i]) == 1:
                res[i] = res[i][0]
            
            return res 

    for i, item in enumerate(res):
        if item == '^':
            ans = res[i - 1] ** res[i + 1]
            
            res[i] = ans
            
            del res[i + 1]
            del res[i - 1]

            return res


    for i, item in enumerate(res):
        if item == '*' or item == '/':
            if item == '*':
                ans = res[i - 1] * res[i + 1]
            else:
                ans = res[i - 1] / res[i + 1]

            res[i] = ans

            del res[i + 1]
            del res[i - 1]

            return res

    for i, item in enumerate(res):
        if item == '+' or item == '-':
            if item == '+':
                ans = res[i - 1] + res[i + 1]
            else:
                ans = res[i - 1] - res[i + 1]

            res[i] = ans

            del res[i + 1]
            del res[i - 1]

            return res
