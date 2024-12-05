import ply.lex as lex

tokens = (
    "PLUS",
    "MINUS",
    "NUMBER"
)

t_PLUS = r"\+"
t_MINUS = r"-"

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)  
    return t

t_ignore = " \t"

def t_error(t):
    print(f"Illegal character : {t.val[0]}")
    t.lexer.skip(1)

def t_newline(t):
    r"\n+"
    t.lexer.lineno = len(t.value)

lexer = lex.lex()

data = "2 + 3 - 4"

if(__name__ == "__main__"):


    lexer.input(data)

    while(True):

        token = lexer.token()

        if(not token):
            break

        print(token)
