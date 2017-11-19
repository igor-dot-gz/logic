'''
MIT License

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
'''

class logic:

    def AND(a=0,b=0):
        if a == 1 and b == 1:
            out_and = 1
        else:
            out_and = 0

    def OR(a=0,b=0):
        if a == 1 or b == 1:
            out_or = 1
        else:
            out_or = 0

    def NOT(a=0):
        if a == 1:
            out_not = 0
        else:
            out_not = 1

    def NAND(a=0,b=0):
        if a == 1 and b == 1:
            out_nand = 0
        else:
            out_nand = 1

    def NOR(a=0,b=0):
        if a == 1 and b == 1:
            out_nor = 0
        else:
            out_nor = 1

    def XOR(a=0,b=0):
        if (a == 1 and b == 1) or (a == 0 and b == 0):
            out_xor = 0
        else:
            out_xor = 1

    def XNOR(a=0,b=0):
        if (a == 1 and b == 1) or (a == 0 and b == 0):
            out_xnor = 1
        else:
            out_xnor = 0
