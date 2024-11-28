no_frame = int(input("Enter number of frame: "))
z = ""
for i in range(no_frame):
    x = input(f"Enter frame {i}:")
    z = z + str(len(x)) + x
print(z)