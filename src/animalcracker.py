def animal_crackers(str1):
    new_str = str1.split()
    if len(new_str) == 2:
        if new_str[0][0] == new_str[1][0]:
            return "Yes"
        else:
            return "No"
    else:
        print("Please give two word string")

my_string = "happy hippo"
print(animal_crackers(my_string))
