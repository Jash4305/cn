# Return 0 if even else return 1 
def isEven(sum):
    return 0 if sum % 2 == 0 else 1

def generate_hamming_code(data):
    if len(data) != 4:
        print("The message length should be of length 4")
        return
    
    td = [None] * 7
    td[2] = data[0]
    td[4] = data[1]
    td[5] = data[2]
    td[6] = data[3]

    td[0] = isEven(td[2] + td[4] + td[6])
    td[1] = isEven(td[2] + td[5] + td[6])
    td[3] = isEven(td[4] + td[5] + td[6])

    print("Transmitted Code is:", td)

def check_error(td):
    if len(td) != 7:
        print("The message length should be of length 7")
        return
    p1 = isEven(td[2] + td[4] + td[6] + td[0])
    p2 = isEven(td[2] + td[5] + td[6] + td[1])
    p4 = isEven(td[4] + td[5] + td[6] + td[3])

    error_position_b = f"{p1}{p2}{p4}"
    error_position_d = int(error_position_b, 2)
    print(error_position_b)
    print(error_position_d)

    if td[error_position_d - 1] == 1:
        td[error_position_d - 1] = 0
    else:
        td[error_position_d - 1] = 1
    print("Corrected Data", td)

# Input handling
data1 = input("Enter the data: ")
data = list(map(int, data1))
# generate_hamming_code(data)
check_error(data)