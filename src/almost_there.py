def almost_there(num):
    x = abs(100-num)
    y = abs(200-num)
    if x <=10 or y<=10:
        return "True"
    else:
        return "False"
