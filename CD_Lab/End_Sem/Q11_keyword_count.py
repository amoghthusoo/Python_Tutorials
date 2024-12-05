import ply.lex as lex

tokens = (
    "DEF",
    "RETURN",
    "IF",
    "ELIF",
    "ELSE"
)

t_DEF = r'def'
t_RETURN = r'return'
t_IF = r'if'
t_ELIF = r'elif'
t_ELSE = r'else'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

if(__name__ == "__main__"):
    
    with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\End_Sem\Q11.txt", "r") as f:
        data = f.read()

    print("\nInput String:")
    for i in range(50):
        print("-", end="")
        if(i == 49):
            print()
    print(data)
    for i in range(50):
        print("-", end="")
        if(i == 49):
            print()
    
    lexer.input(data)

    def_count = 0
    return_count = 0
    if_count = 0
    elif_count = 0
    else_count = 0
    
    while True:
        
        token = lexer.token()
        
        if not token:
            break
        
        if(token.type == "DEF"):
            def_count += 1
        elif(token.type == "RETURN"):
            return_count += 1
        elif(token.type == "IF"):
            if_count += 1
        elif(token.type == "ELIF"):
            elif_count += 1
        elif(token.type == "ELSE"):
            else_count += 1

    print()
    print(f"No. of def keyword : {def_count}")
    print(f"No. of return keyword : {return_count}")
    print(f"No. of if keyword : {if_count}")
    print(f"No. of elif keyword : {elif_count}")
    print(f"No. of else keyword : {else_count}")
    print()
