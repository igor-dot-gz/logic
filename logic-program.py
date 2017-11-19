print("0s and 1s only!")
a = int(input("Input A = "))
b = int(input("Input B = "))

#AND
if a == 1 and b == 1:
    print("AND ---> 1")
else:
    print("AND ---> 0")

#OR
if a == 1 or b == 1:
    print("OR ----> 1")
else:
    print("OR ----> 0")

#NOT, ignores b
if a == 1:
    print("NOT ---> 0")
else:
    print("NOT ---> 1")

#NAND
if a == 1 and b == 1:
    print("NAND --> 0")
else:
    print("NAND --> 1")

#NOR
if a == 1 and b == 1:
    print("NOR ---> 0")
else:
    print("NOR ---> 1")

#XOR / EXOR
if (a == 1 and b == 1) or (a == 0 and b == 0):
    print("XOR ---> 0")
else:
    print("XOR ---> 1")

#XNOR / EXNOR
if (a == 1 and b == 1) or (a == 0 and b == 0):
    print("XNOR --> 1")
else:
    print("XNOR --> 0")
