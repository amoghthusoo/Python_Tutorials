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
    
    with open(r"C:\Users\Dell\Desktop\Python_Tutorials\CD_Lab\Lex_Yacc\text.txt", "r") as f:
        data = f.read()

    # print(data)
    
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
