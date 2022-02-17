def black_jack(a,b,c):
    sum_num= a+b+c
    if (sum_num <= 21):
        return sum_num
    elif sum_num>21 and 11 in (a,b,c):
        return sum_num-10
    else :
        return "bust"
