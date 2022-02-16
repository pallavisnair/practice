#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
#if both numbers are even, but returns the greater if one or both numbers are odd

def odd_even_comparison(x,y):
    if x%2==0 and y%2==0:
        if x>y:
            return y
    elif x%2 == 1 or y%2==1:
        if x>y:
            return x

print(odd_even_comparison(7,5))
