import ply.lex as lex

tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
)

t_PLUS = r"\+"
t_MINUS = r"-"

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

data = """2 + 34 - 1"""

if(__name__ == "__main__"):

    lexer.input(data)

    print()

    for _ in range(45):
        print("-", end="")
    print()

    print(f"|   Type   |   Value  | Line No. |  Lex Pos |")

    for _ in range(45):
        print("-", end="")
    print()

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"|{tok.type:^10}|{tok.value:^10}|{tok.lineno:^10}|{tok.lexpos:^10}|")       
    
    for _ in range(45):
        print("-", end="")
    print()
    print()
