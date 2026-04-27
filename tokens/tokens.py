# Token Types (TT)
TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_STRING = 'TT_STRING'
TT_IDENT = 'TT_IDENT'


# Keywords (assignment, io, ctrl-flow)
TT_GURT = 'TT_GURT' # set
TT_YO = 'TT_YO' # =
TT_YAP = 'TT_YAP' # print
TT_TS = 'TT_TS' # if
TT_PMO = 'TT_PMO' # else
TT_MEWSTREAK = 'TT_MEWSTREAK' # while
TT_EDGE = 'TT_EDGE' # continue
TT_GOON = 'TT_GOON' # break
TT_NOT = 'TT_NOT' # boolean not


# Bool Lit
TT_ONG = 'TT_ONG' # True
TT_CAP = 'TT_CAP' # False


# Arithmetic Ops
TT_BUFF = 'TT_BUFF' # +
TT_NERF = 'TT_NERF' # -
TT_FANUMTAX = 'TT_FANUMTAX' # *
TT_RATIO = 'TT_RATIO' # /
TT_TWIN = 'TT_TWIN' # ==
TT_MOGGED = 'TT_MOGGED' # >
TT_CHOPPED = 'TT_CHOPPED' # <


# Delims / Block
TT_LPAREN = 'TT_LPAREN' # (
TT_RPAREN = 'TT_RPAREN' # )
TT_BLOCK_START = 'TT_BLOCK_START' # 6ix (opening block)
TT_BLOCK_END = 'TT_BLOCK_END' # 7even (closing block)


# Stmt Term Chars
TT_SYBAU = 'TT_SYBAU' # newline -> ; in cpp
TT_EOF = 'TT_EOF'


# Maps for Lexer
# Keywords
KEYWORDS = {
    'gurt': TT_GURT,
    'yo': TT_YO,
    'yap': TT_YAP,
    'ts': TT_TS,
    'pmo': TT_PMO,
    'mewstreak': TT_MEWSTREAK,
    'edge': TT_EDGE,
    'goon': TT_GOON,
    'not': TT_NOT,
    'ong': TT_ONG,
    'cap': TT_CAP,
    '6ix': TT_BLOCK_START,
    '7even': TT_BLOCK_END,
}


# Ops
OPERATORS = {
    'buff': TT_BUFF,
    'nerf': TT_NERF,
    'fanumtax': TT_FANUMTAX,
    'ratio': TT_RATIO,
    'twin': TT_TWIN,
    'mogged': TT_MOGGED,
    'chopped': TT_CHOPPED,
}

class Tokens:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value:
            return f'{self.type}: {self.value}'
        else:
            # no value
            return f'{self.type}'