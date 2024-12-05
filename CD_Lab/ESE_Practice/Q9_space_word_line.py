import ply.lex as lex

tokens = (
    "SPACE",
    "WORD"
)

t_SPACE = r"\s"
t_WORD = r"""[A-Za-z,.!?'"]+"""

def t_error(t):
    print(f"Illegal token : {t.value[0]}")
    t.lexer.skip(1)

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\ESE_Practice\data3.txt", "r") as f:
    data = f.read()

lexer.input(data)

space_count = 0
word_count = 0
line_count = 0

while True:

    token = lexer.token()

    if(not token):
        break

    if(token.type == "SPACE"):
        space_count += 1
    elif(token.type == "WORD"):
        word_count += 1
    
    last_token = token

try:
    line_count = last_token.lineno
except:
    pass

print(f"Total no. of spaces are : {space_count}")
print(f"Total no. of words are : {word_count}")
print(f"Total no. of lines are : {line_count}")
