import ply.lex as lex

tokens = (
    "OPERATOR",
)

t_OPERATOR = r"(\+|\-|\*|/|==|=)"

def t_error(t):
    # print(f"Illegal token : {t.value[0]}")
    t.lexer.skip(1)

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


lexer = lex.lex()

with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\ESE_Practice\data2.txt", "r") as f:
    data = f.read()

lexer.input(data)

operator_count = 0

while(True):

    token = lexer.token()

    if(not token):
        break

    if(token.type == "OPERATOR"):
        operator_count += 1

print(f"Total no. of operators are : {operator_count}")