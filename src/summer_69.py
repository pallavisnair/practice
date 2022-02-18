def summer_69(arr):
   total = 0
   condition = True
   for num in arr:
       while condition:
           if num != 6:
               total+= num
               break
           else:
               condition = False
       while not condition :
           if num!=9:
                break
           else:
                condition=True
                break
   return total
