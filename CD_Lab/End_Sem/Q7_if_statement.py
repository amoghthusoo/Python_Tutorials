import ply.lex as lex

tokens = (
    "IF",
    "LPAREN",
    "RPAREN",
    "IDENTIFIER",
    "OPERATOR",
    "NUMBER",
    "COLON"
)

t_IF = r'if'
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_NUMBER = r"[0-9.]+"
t_OPERATOR = r'(\+|\-|\*|/|==|=|!=|<=|>=|<|>|&|\||~|and|or|not)'
t_COLON = r':'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    
    if(t.value == "if"):
        t.type = "IF"

    return t

t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

if(__name__ == "__main__"):
    
    with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\End_Sem\Q7.txt", "r") as f:
        data = f.read()

    print("\nInput String:")
    for i in range(51):
        print("-", end="")
        if(i == 50):
            print()
    
    print(data)

    for i in range(51):
        print("-", end="")
        if(i == 50):
            print()
    
    lexer.input(data)

    print()

    for _ in range(51):
        print("-", end="")
    print()

    print(f"|      Type      |   Value  | Line No. |  Lex Pos |")

    for _ in range(51):
        print("-", end="")
    print()

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"|{tok.type:^16}|{tok.value:^10}|{tok.lineno:^10}|{tok.lexpos:^10}|")       
    
    for _ in range(51):
        print("-", end="")
    print()
    print()
