from dataclasses import dataclass
from typing import List, Optional, Any

# Expressions
@dataclass
class Literal:
    # int, float, str, bool
    value: Any
    
@dataclass
class Identifier:
    name: str
    
@dataclass
class BinOp:
    op: str
    left: 'Expr'
    right: 'Expr'

@dataclass
class UnaryOp:
    op: str
    expr: 'Expr'

# Stmts
@dataclass
class Let:
    name: str
    value: 'Expr'

@dataclass
class Print:
    expr: 'Expr'

@dataclass
class If:
    condition: 'Expr'
    then_block: 'Block'
    else_block: Optional['Block']

@dataclass
class While:
    condition: 'Expr'
    body: 'Block'

@dataclass
class Block:
    statements: List['Stmt']

@dataclass
class Break:
    pass

@dataclass
class Continue:
    pass

@dataclass
class ExprStmt:
    expr: 'Expr'

@dataclass
class Program:
    statements: List['Stmt']

# type aliasse
Expr = Literal | Identifier | BinOp | UnaryOp
Stmt = Let | Print | If | While | Block | Break | Continue | ExprStmt