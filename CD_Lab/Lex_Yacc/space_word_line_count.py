import ply.lex as lex

tokens = (
    "WORD",
    "SPACE"
)

t_WORD = r"""[a-zA-Z0-9"'.,?!():;]+"""
t_SPACE = r"\s"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

if(__name__ == "__main__"):
    
    with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\Lex_Yacc\text.txt", "r") as f:
        data = f.read()

    # print(data)

    lexer.input(data)

    word_count = 0
    space_count = 0
    line_count = 0
    while True:
        
        token = lexer.token()
        
        if not token:
            break
        
        if(token.type == "WORD"):
            word_count += 1
        elif(token.type == "SPACE"):
            space_count += 1

        previous_token = token
    
    try:
        line_count = previous_token.lineno
    except:
        pass

    print()
    print(f"No. of blank spaces : {space_count}")
    print(f"No. of words : {word_count}")
    print(f"No. of lines : {line_count}")
    print()