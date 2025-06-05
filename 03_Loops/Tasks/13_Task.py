str1 = "P@#yn26at^&i5ve"

alphabets = 0
sp_char = 0
number = 0



for i in range(len(str1)):
    if str1[i].isalpha():
        alphabets += 1
    elif str1[i].isdigit():
        number += 1
    else:
        sp_char += 1


print(f"Given String: {str1} \nAlphabets: {alphabets} \nNumbers: {number} \nSpecial Character: {sp_char}")