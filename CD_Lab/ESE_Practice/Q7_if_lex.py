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

t_IF = r"if"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_OPERATOR = r"<|<=|>|>=|=="
t_NUMBER = r"[0-9]+"
t_COLON = r":"

def t_IDENTIFIER(t):
    r"[_a-zA-Z][_a-zA-Z0-9]*"

    if(t.value == "if"):
        t.type = "IF"
    
    return t

t_ignore = " \t"

def t_error(t):
    print(f"Illegal character : {t.value[0]}")
    t.lexer.skip(1)

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\ESE_Practice\data4.txt", "r") as f:
    data = f.read()

lexer = lex.lex()

lexer.input(data)

while(True):

    token = lexer.token()

    if(not token):
        break

    print(token)
