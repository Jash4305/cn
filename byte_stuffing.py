data = input("Enter the data string : ")
start_flag = input("Enter the start flag :")
end_flag = input("Enter the end flag :")
escape_char = input("Enter the escape char : ")
stuffed_char = f"{start_flag}"

for char in data:
    if char == end_flag or char == start_flag:
        stuffed_char += escape_char + char
    else:
        stuffed_char += char
print(stuffed_char + end_flag)