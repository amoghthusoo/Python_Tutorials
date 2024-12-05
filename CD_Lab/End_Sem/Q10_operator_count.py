import ply.lex as lex

tokens = (
    "OPERATOR",
)

t_OPERATOR = r'(\+|\-|\*|/|==|=|!=|<=|>=|<|>|&|\||~|and|or|not)'

def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if(__name__ == "__main__"):
    
    with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\End_Sem\Q10.txt", "r") as f:
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

    operator_count = 0
    while True:
        
        token = lexer.token()
        
        if not token:
            break
        
        if(token.type == "OPERATOR"):
            operator_count += 1

    print()
    print(f"No. of operators : {operator_count}")
    print()
