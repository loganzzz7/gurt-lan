from tokens.tokens import *

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.curr_char = None
        # start idx at 0
        self.traverse()
    
    
    def traverse(self):
        self.pos += 1
        self.curr_char = self.text[self.pos] if self.pos < len(self.text) else None
    
    
    def is_al_num(self, c):
        return (ord("a") <= ord(c) <= ord("z") or
                ord("A") <= ord(c) <= ord("Z") or
                ord("0") <= ord(c) <= ord("9"))
    
    def read_word(self):
        word = ""
        while self.curr_char and self.is_al_num(self.curr_char):
            word += self.curr_char
            self.traverse()
        return word
    
    
    def read_number(self):
        number = ""
        numType = "int"
        while self.curr_char and self.curr_char.isdigit():
            number += self.curr_char
            self.traverse()
            if self.curr_char == "." and (self.pos + 1) < len(self.text) and self.text[self.pos + 1].isdigit():
                numType = "float"
                number += self.curr_char
                self.traverse()
        return int(number) if numType == "int" else float(number)
                
                
    def create_tokens(self):
        tokens = []
        
        while self.curr_char is not None:
            if self.curr_char in ' \t':
                self.traverse()
            # newline case -> stmt term = sybau
            elif self.curr_char == '\n':
                tokens.append(Tokens(TT_SYBAU, '\n'))
                self.traverse()
            # alnum word
            elif self.curr_char.isalpha():
                word = self.read_word()
                if word in KEYWORDS:
                    tokens.append(Tokens(KEYWORDS[word], word))
                elif word in OPERATORS:
                    tokens.append(Tokens(OPERATORS[word], word))
                else:
                    # ident
                    tokens.append(Tokens(TT_IDENT, word))
            # numbers
            elif self.curr_char.isdigit():
                num = self.read_number()
                if isinstance(num, int):
                    tokens.append(Tokens(TT_INT, num))
                elif isinstance(num, float):
                    tokens.append(Tokens(TT_FLOAT, num))
            # single char delim/ops
            elif self.curr_char == '(':
                tokens.append(Tokens(TT_LPAREN, '('))
                self.traverse()
            elif self.curr_char == ')':
                tokens.append(Tokens(TT_RPAREN, ')'))
                self.traverse()
            else:
                # unknown... skip
                self.traverse()
        tokens.append(Tokens(TT_EOF, None))
        return tokens
