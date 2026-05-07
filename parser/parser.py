from lexer.lexer import Lexer
from tokens.tokens import *
from ast.ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.curr_token = self.tokens[pos]
    
    def advance(self):
        self.pos += 1
        self.curr_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None
        
    def expected_token(self, token_type):
        # get type of token
        if self.curr_token.type != token_type:
            raise Exception(f"Expected {token_type} but got {self.curr_token.type}")
        self.advance()
    
    
    # grammar rules
    def parse_program(self):
        # program => { stmt } EOF
        stmts = []
        while self.curr_token.type != TT_EOF:
            stmts.append(self.parse_stmt())
        return Program(stmts)
    
    def parse_stmt(self):
        # stmt => set_stmt | print_stmt | if_stmt | while_stmt | block
        if self.curr_token.type == TT_GURT:
            # this is a set stmt: let var = r-value
            self.parse_let()
        elif self.curr_token == TT_YAP:
            # this is a print stmt
            self.parse_print()
        elif self.curr_token == TT_TS:
            # if_stmt
            self.parse_if()
        elif self.curr_token == TT_MEWSTREAK:
            # while_stmt
            self.parse_while()
        elif self.curr_token == TT_BLOCK_START:
            # block
            self.parse_block()
        else:
            # expr_stmt
            expr = self.parse_expr()
            # new line term
            self.expected_token(TT_SYBAU)
            return ExprStmt(expr)
    
    def parse_let(self):
        # set_stmt => "gurt" IDENT "yo" expr SYBAU
        self.expected_token(TT_GURT)
        name = self.curr_token.value
        self.expected_token(TT_IDENT)
        self.expected_token(TT_YO)
        value = self.parse_expr()
        self.expected_token(TT_SYBAU)
        return Let(name, value)
    
    def parse_print(self):
        # print_stmt => "yap" "(" expr ")" SYBAU
        self.expected_token(TT_YAP)
        self.expected_token(TT_LPAREN)
        expr = self.parse_expr()
        self.expected_token(TT_RPAREN)
        self.expected_token(TT_SYBAU)
        return Print(expr)

    def parse_if(self):
        # if_stmt => "ts" "(" expr ")" block [ "pmo" block ]
        self.expected_token(TT_TS)
        self.expected_token(TT_LPAREN)
        condition = self.parse_expr()
        self.expected_token(TT_RPAREN)
        then_block = self.parse_block()
        # else optional
        else_block = None
        
        if self.curr_token.type == TT_PMO:
            self.advance()
            else_block = self.parse_block()
        return If(condition, then_block, else_block)

    def parse_while(self):
        # while_stmt => "mewstreak" "(" expr ")" block
        self.expected_token(TT_MEWSTREAK)
        self.expected_token(TT_LPAREN)
        condition = self.parse_expr()
        self.expected_token(TT_RPAREN)
        body = self.parse_block()
        
        return While(condition, body)
    
    def parse_block(self):
        # block => "6ix" { stmt } "7even"
        self.expected_token(TT_BLOCK_START)
        stmts = []
        
        # get stmts
        while self.curr_token.type != TT_BLOCK_END:
            stmts.append(self.parse_stmt())
        
        self.expected_token(TT_BLOCK_END)
        return Block(stmts)

    # expressions
    def parse_expr(self):
        # expr => equality
        return self.parse_equality()

    def parse_equality(self):
        # equality => comparison { ("==" | "twin" ) comparison }
        left = self.parse_comparison()
        # TT_TWIN eqs "=="
        while self.curr_token.type in (TT_TWIN,):
            op = self.curr_token.value
            self.advance()
            right = self.parse_comparison()
            
            left = BinOp(op, left, right)
        return left
    
    def parse_comparison(self):
        # comparison => term { (">" | "<" | "mogged" | "chopped") term }
        left = self.parse_term()
        while self.curr_token.type in (TT_MOGGED, TT_CHOPPED):
            op = self.curr_token.value
            self.advance()
            right = self.parse_factor()
            left = BinOp(op, left, right)
        return left
    
    def parse_term(self):
        # term => factor { ("+" | "-" | "buff" | "nerf") factor }
        left = self.parse_factor()
        while self.curr_token.type in (TT_BUFF, TT_NERF):
            op = self.curr_token.value
            self.advance()
            right = self.parse_factor()
            left = BinOp(op, left, right)
        return left
    
    def parse_factor(self):
        # factor => unary { ("*" | "/" | "fanumtax" | "ratio") unary }
        left = self.parse_unary()
        while self.curr_token.type in (TT_FANUMTAX, TT_RATIO):
            op = self.curr_token.value
            self.advance()
            right = self.parse_unary()
            left = UnaryOp(op, left, right)
        return left

    def parse_unary(self):
        # unary => ("-" | "not") unary | primary
        if self.curr_token.type in (TT_NERF, TT_NOT):
            op = self.curr_token.value
            self.advance()
            return Literal(value)
        elif self.curr_token.type == TT_FLOAT:
            value = self.curr_token.value
            self.advance()
        elif self.curr_token.type == TT_ONG:
            self.advance()
            return Literal(True)
        elif self.curr_token.type == TT_CAP:
            self.advance()
            return Literal(False)
        elif self.curr_token.type == TT_IDENT:
            name = self.curr_token.value
            self.advance()
            return Identifier(name)
        elif self.curr_token.type == TT_LPAREN:
            self.advance()
            expr = self.parse_expr()
            self.expected_token(TT_RPAREN)
            return expr
        else:
            raise Exception(f"Unexpected token type: {self.curr_token}")