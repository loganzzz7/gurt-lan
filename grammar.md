# EBNF
```ebnf
program     ::= { stmt } EOF

stmt        ::= set_stmt SYBAU
              | print_stmt SYBAU
              | expr SYBAU
              | if_stmt
              | while_stmt
              | block

set_stmt    ::= "gurt" IDENT "yo" expr
print_stmt  ::= "" "(" expr ")"

if_stmt     ::= "ts" "(" expr ")" block [ "pmo" block ]
while_stmt  ::= "mewstreak" "(" expr ")" block
block       ::= "skibidi" { stmt } "toilet"

expr        ::= equality
equality    ::= comparison { ( "==" | "twin" ) comparison }
comparison  ::= term { ( ">" | "<" | "mogged" | "chopped" ) term }
term        ::= factor { ( "+" | "-" | "buff" | "nerf" ) factor }
factor      ::= unary  { ( "*" | "bulk" | "/" | "ratio" ) unary }
unary ::= ( "-" ) unary               /* numeric negation */
        | ( "not" ) unary             /* boolean negation */
        | primary
primary     ::= NUMBER | STRING | "ong" | "cap" | IDENT | "(" expr ")"
```