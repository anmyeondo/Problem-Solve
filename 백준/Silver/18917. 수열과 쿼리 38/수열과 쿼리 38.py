from sys import stdin


tc = int(stdin.readline())
s = 0
xor = 0

for _ in range(tc):
    input_data = list(map(int, stdin.readline().split()))

    if len(input_data) == 1:
        command = input_data[0]
    else:
        command, n = input_data[0], input_data[1]
    
    if command == 1:
        s += n
        xor = xor ^ n 
    elif command == 2:
        s -= n
        xor = xor ^ n
    elif command == 3:
        print(s)
    elif command == 4:
        print(xor)
