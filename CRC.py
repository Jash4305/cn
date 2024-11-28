def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def binary_division(dividend, divisor):
    pick = len(divisor)
    temp = dividend[:pick]

    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[pick]
        else:
            temp = xor('0' * pick, temp) + dividend[pick]
        pick += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)
    return temp
    
def encode_data(data, divisor):
    n = len(divisor) - 1
    appended_data = data + '0' * n
    remainder = binary_division(appended_data, divisor)
    codeword = data + remainder
    return codeword

data = input("Enter the data to be sent: ")
divisor = input("Enter the divisor: ")
print("Coded msg:", encode_data(data, divisor))
received_data = input("Enter the data to be received: ")
rdivisor = input("Enter the divisor: ")
checkerror = binary_division(received_data, rdivisor)
if '1' in checkerror:
    print("Error Detected")
else:
    print("Correct Code")