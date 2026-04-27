# Goal: convert a sequence of characters into a sequence of lexical  tokens
# references ebnf to read .gurt into correct symbol to char grp matching
# use regex to filter chars
import re
from readToken import readToken

def lexer(script):
    input = readToken(script)
    while input.next is not None:
        if input == " ":
            input = input.moveNext()
        elif input:
            return input
            

def main():
    code = "testing bruh"
    print(lexer(code))

if __name__ == "__main__":
    main()