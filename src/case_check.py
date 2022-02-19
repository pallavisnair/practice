def case_check(my_line):
    d = {"upper":0,"lower":0}
    for letter in my_line:
        if letter.isupper():
            d["upper"]+=1
        elif letter.islower():
            d["lower"]+=1
        else:
            pass
    print("no. of upper case :{} ".format(d["upper"]))
    print("no. of lower case :{} ".format(d["lower"]))

