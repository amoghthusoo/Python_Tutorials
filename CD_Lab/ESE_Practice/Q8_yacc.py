import ply.yacc as yacc
from Q8_lex import tokens, data

def p_r1(p):
    "E : E PLUS T"

def p_r2(p):
    "E : E MINUS T"

def p_r3(p):
    "E : T"

def p_r4(p):
    "T : NUMBER"

def p_error(p):
    print("Syntax error in input.")

if(__name__ == "__main__"):

    parser = yacc.yacc()
    parser.parse(data)

