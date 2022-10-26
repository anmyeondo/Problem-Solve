def scan_input():
    temp = input()
    arr = temp.split(" ")
    return arr

scanArr = scan_input()
A, B = int( scanArr[0] ), int( scanArr[1] )

if 0 < A < 10 and 0 < B < 10:
    print(A+B)
else:
    print("error")