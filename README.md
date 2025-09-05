# .gurt Overview
1. **grammar.md** — tokens + EBNF + examples.
2. **lexer.py** — tokenize(src) -> [Token].
3. **ast_nodes.py** — dataclasses for nodes.
4. **parser.py** — produces AST + error recovery.
5. **semantics.py** — scope + simple checks.
6. **codegen.py** — Python emitter (string or ast module).
7. **cli.py** — run|build commands.
8. **tests/** — unit + golden + error tests.
9. **examples/** — the sample programs` scoped in step 0.

## Scope (Features):
| .py | .gurt |
| -------- | ------- |
| print | yo |
| if | ts |
| else | pmo |
| while | mewstreak |
| == | twin|
| new-line | sybau |
| > (greater than) | mogged |
| < (lesser than) | chopped |
| + (add) | buff |
| - (subtract) | nerf |
| True | ong |
| False | cap |

### TODO Additional Features:
| .py | .gurt |
| -------- | ------- |
| continue | edge |
| break | goon |

## TODO EBNF (grammar):
- Define tokens & grammar in EBNF.
- Lock in keywords, operators, whitespace/comments, and error sync points (; and }).

## TODO Tokenizer / Lexer (Written in Python):
- Implement a hand-rolled lexer in Python that:
    - Streams characters → tokens with type, lexeme, value, line, col.
    - Handles identifiers/keywords, numbers, strings, operators, delimiters, comments.
- Tests: property tests for “round trip” on operators/keywords; fuzz a few random inputs; assert line/column tracking.

## TODO Parser -> Concrete Syntax Tree -> Abstract Syntax Tree (Written in Python):
- Hand-written recursive-descent.
- Build small node classes with @dataclass, e.g. Let(name, expr), If(cond, then_block, else_block), While(cond, body), BinOp(op, left, right), Literal(value), Var(name), Block(stmts).
- Implement a parse error strategy: on error, advance to next ; or } and continue to collect more errors.

## TODO Semantic Analysis:
- Implement a simple pass over the AST:
    - **Symbol table / scopes** (stack): declare on let, resolve on Var.
    <!-- - Basic type checks (optional for a toy language; at least catch use-before-define). -->
    <!-- - Desugarings if you want (e.g., rewrite != into not (==)). -->
- Emit friendly diagnostics with line/column.

## TODO Code Generation -> Python (Written in Python):
**Generate Python source strings**
- Write a CodeGen visitor that turns each AST node into Python code with indentation management.
- Example mappings:
    - let x = 5; → x = 5
    - yo(expr); → print(expr)
    - ts (c) { ... } pmo { ... } → if c:\n ...\nelse:\n ...
    - mewstreak (c) { ... } → while c:\n ...

## CLI, Runner, Tests:
- mytoy run file.toy → transpiles to Python → runs it.
- mytoy build file.toy -o out.py → writes Python file.
- Tests:
    - **Golden tests**: input .toy → expected Python text (or expected stdout).
    - **Round-trip smoke**: run the generated Python and compare outputs to expected.
    - Error tests: malformed inputs that should raise clear diagnostics.