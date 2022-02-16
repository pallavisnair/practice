def string_case(word):
    result = ""
    length = len(word)
    for i in range(0,length-1,2):
        result += word[i].lower()+word[i+1].upper()
    if length % 2 ==1:
        result += word[length-1].lower()
    return result
