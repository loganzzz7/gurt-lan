from lexer.lexer import Lexer

test_str = """
gurt x yo 42
"""

lexer = Lexer(test_str)
tokens = lexer.create_tokens()

for token in tokens:
    print(f"token: {token}")
