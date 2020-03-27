"""
Program to simulate tokenizer in Python

@author: D Samuel Joshua Viswas

Please do feel free to shareand modify the code.
"""
import sys

keywords = { 'int', 'float', 'double', 'long', 'auto', 'const', 'struct', 'unsigned', 'double', 'break', 'continue',
            'signed', 'switch', 'void', 'else', 'for', 'case', 'default', 'register', 'sizeof',
            'typedef', 'volatile', 'enum', 'goto', 'char', 'do', 'return', 'static', 'union', 'while', 'extern', 'if' }

    operators = { '+', '-', '*', '/', '%', '++', '--', '=', '+=', '-=', '*=', '/=', '%=', '==', '>', '<', '!=', '>=', '<=',
                 '&&', '||', '!', '&', '|', '^', '<<', '>>', '~' }

    arr = []

    print('Enter an input')
    n = sys.stdin.readlines()

    for i in range(len(n)) :
        n[i] = n[i].rstrip("\n")
        print("appending to the list")
        arr.append(n[i].split(" "))

        for i in range(len(arr)) :
            for j in range(len(arr[i])) :
                if arr[i][j] in keywords :
print('KEYWORD --> ', arr[i][j])
elif arr[i][j] in operators :
print('OPERATOR --> ', arr[i][j])
elif arr[i][j].isdigit() :
    print('VALUE --> ', arr[i][j])
                else:
print('Variable -->', arr[i][j])
