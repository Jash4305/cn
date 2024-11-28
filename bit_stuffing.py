string =input("Enter the message sent:")
new_string = ''
c = 0
for i in string:
    new_string+= i
    if i == '1':
        c+= 1
    else:
        c = 0
    if c == 5:
        new_string += '0'
        c = 0
print(new_string)


