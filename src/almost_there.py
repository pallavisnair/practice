def almost_there(num):
    x = 100-num
    y = 200-num
    if x in range(0,11) or y in range(0,11):
        return "True"
    else:
        return "False"
