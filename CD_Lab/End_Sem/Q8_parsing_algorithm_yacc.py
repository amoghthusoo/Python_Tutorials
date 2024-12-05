import ply.yacc as yacc
from Q8_parsing_algorithm_lex import tokens, data

def p_expr_plus_minus(p):
    '''expr : expr PLUS term
            | expr MINUS term'''

def p_expr_term(p):
    'expr : term'

def p_term_number(p):
    'term : NUMBER'

def p_error(p):
    print("Syntax error in input!")


if(__name__ == "__main__"):

    print()
    parser = yacc.yacc()

    parser.parse(data)
    print("Execution completed!")
    print()
