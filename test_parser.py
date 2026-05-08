from lexer.lexer import Lexer
from parser.parser import Parser

test_code = """
gurt x yo 42
"""

lexer = Lexer(test_code)
tokens = lexer.create_tokens()
parser = Parser(tokens)
ast = parser.parse_program()

# Program(statements=[Let(name='x', value=Literal(value=42))])
print(ast)