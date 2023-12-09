

text = list("dabAcCaCBAcCcaDA")
new_list = []

for i in range(0, len(text)-1):
    print('---',i, text[i], text[i+1])
    if text[i] != text[i+1]:
        if text[i].upper() == text[i+1].upper():
            print(text[i], text[i+1])
        else:
            new_list.extend([text[i], text[i+1]])
    else:
        new_list.append(text[i])
     

print(text)
print(new_list)
   # print(text[i], text[i].isupper() )