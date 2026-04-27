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
    
    
    def read_word(self):
        word = ""
        while self.curr_char and self.curr_char.is_al_num():
            word += self.curr_char
            self.traverse()
        return word
    
    
    def is_al_num(self):
        return (ord("a") <= ord(self.curr_char) <= ord("z") or
                ord("A") <= ord(self.curr_char) <= ord("Z") or
                ord("0") <= ord(self.curr_char) <= ord("9"))
    
    
    def create_tokens(self):
        tokens = []
        
        while self.curr_char is not None:
            if self.curr_char in ' \t':
                self.traverse()
            # newline case -> stmt term = sybau
            elif self.curr_char == '\n':
                tokens.append(Tokens(TT_SYBAU, '\n'))
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
            elif self.curr_char == ')':
                tokens.append(Tokens(TT_RPAREN, ')'))
            else:
                # unknown... skip
                self.traverse()
        tokens.append(Tokens(TT_EOF, None))
        return tokens
