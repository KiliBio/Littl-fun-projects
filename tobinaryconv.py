'''
Converts decimal numbers into binary numbers
'''
"""

00000000 = 0
00000001 = 1
00000010 = 2
00000011 = 3
00000100 = 4
00000101 = 5
00000110 = 6
00000111 = 7
00001000 = 8
00001001 = 9
00001010 = 10

"""
binary = ['']

def tobinary(num):
    x = 4294967296
    print (num, x)
    if num > x:
        print("Number out of range for this function.")
    else:
        while x > 0:
            print (x)
            if num // x == 1:
                binary.append('1')
                num = num - x
                x = x // 2
                print ("if", binary)
            else:
                binary.append('0')
                x = x // 2
                print("else", binary)
    print(''.join(binary))

tobinary(294967341)