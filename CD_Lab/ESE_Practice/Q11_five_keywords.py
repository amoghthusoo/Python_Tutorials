import ply.lex as lex

tokens = (
    "IF",
    "ELIF",
    "ELSE",
    "DEF",
    "RETURN",
)

t_IF = r"if"
t_ELIF = r"elif"
t_ELSE = r"else"
t_DEF = r"def"
t_RETURN = r"return"

def t_error(t):
    t.lexer.skip(1)

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\ESE_Practice\data.txt", "r") as f:
    data = f.read()

lexer = lex.lex()
lexer.input(data)

if_count = 0
elif_count = 0
else_count = 0
def_count = 0
return_count = 0

while True:

    token = lexer.token()

    if(not token):
        break

    
    if(token.type == "IF"):
        if_count += 1
    elif(token.type == "ELIF"):
        elif_count += 1
    elif(token.type == "ELSE"):
        else_count += 1
    elif(token.type == "DEF"):
        def_count += 1
    elif(token.type == "RETURN"):
        return_count += 1

print(f"No. of if keyword : {if_count}")
print(f"No. of elif keyword : {elif_count}")
print(f"No. of else keyword : {else_count}")
print(f"No. of def keyword : {def_count}")
print(f"No. of return keyword : {return_count}")
