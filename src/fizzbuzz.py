my_list=[]
for x in range(1,100):
    if (x % 3 == 0 and x % 5 == 0):
        my_list.append("fizzbuzz")
    elif (x % 3 ==0 ):
        my_list.append("fizz")
    elif (x % 5 == 0):
        my_list.append("buzz")
    else:
        my_list.append(x)
print(my_list)
