__slots__ = ["version", "a", "b"]
version = "0.5c"

### OTHER

def help():
    print("logic.    (       )")
    print("      AND  a=0,b=0")
    print("      OR   a=0,b=0")
    print("      NOT  a=0")
    print("      NAND a=0,b=0")
    print("      NOR  a=0,b=0")
    print("      XOR  a=0,b=0")
    print("      XNOR a=0,b=0")

def ver():
    print(version)

def license():
    print('''
    MIT License+




    Copyright (c) 2017 Igor Smolinski

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    ''')

### LOGIC GATES
def AND(a,b):
    if a == 1 and b == 1:
        return True
    else:
        return False

def OR(a,b):
    if a == 1 or b == 1:
        return True
    else:
        return False

def NOT(a):
    if a == 1:
        return False
    else:
        return True

def NAND(a,b):
    if a == 1 and b == 1:
        return False
    else:
        return True

def NOR(a,b):
    if a == 1 and b == 1:
        return False
    else:
        return True

def XOR(a,b):
    if (a == 1 and b == 1) or (a == 0 and b == 0):
        return False
    else:
        return True

def XNOR(a,b):
    if (a == 1 and b == 1) or (a == 0 and b == 0):
        return True
    else:
        return False
