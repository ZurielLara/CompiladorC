# -*- enconding: utf-8 -*-
#!/usr/bin/python
import ply.yacc as yacc
import os
from c_lexer import tokens
import sys


VERBOSE = 1


def p_program(p):
    'program : declaration_list'
    pass


def p_declaration_list_1(p):
    'declaration_list : declaration_list declaration'
    pass


def p_declaration_list_2(p):
    'declaration_list : declaration'
    pass


def p_declaration(p):
    '''declaration : var_declaration
    | fun_declaration
    | HASH INCLUDE LESS ID GREATER
    | USING NAMESPACE STD SEMICOLON'''
    pass


def p_var_declaration_1(p):
    '''var_declaration : type_specifier ID SEMICOLON
    | type_specifier ID COMMA ID SEMICOLON
    | type_specifier ID EQUAL NUMBER SEMICOLON
    | type_specifier ID EQUAL var SEMICOLON
    '''
    pass


def p_var_declaration_2(p):
    'var_declaration : type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLON'
    pass


def p_type_specifier_1(p):
    'type_specifier : INT'
    pass


def p_type_specifier_2(p):
    'type_specifier : VOID'
    pass


def p_type_specifier_(p):
    'type_specifier : STRING'
    pass


def p_fun_declaration(p):
    'fun_declaration : type_specifier ID LPAREN params RPAREN compount_stmt'
    pass


def p_params_1(p):
    'params : param_list'
    pass


def p_params_2(p):
    'params : VOID'
    pass


def p_param_list_1(p):
    'param_list : param_list COMMA param'
    pass


def p_param_list_2(p):
    'param_list : param'
    pass


def p_param_list_3(p):
    'param_list : empty'
    pass


def p_param_1(p):
    'param : type_specifier ID'
    pass


def p_param_2(p):
    'param : type_specifier ID LBRACKET RBRACKET'
    pass


def p_compount_stmt(p):
    'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
    pass


def p_local_declarations_1(p):
    'local_declarations : local_declarations var_declaration'
    pass


def p_local_declarations_2(p):
    'local_declarations : empty'
    pass


def p_statement_list_1(p):
    'statement_list : statement_list statement'
    pass


def p_statement_list_2(p):
    'statement_list : empty'
    pass


def p_statement(p):
    '''statement : expression_stmt
            | compount_stmt
            | selection_stmt
            | iteration_stmt
            | return_stmt
    '''
    pass


def p_expression_stmt_1(p):
    '''expression_stmt : expression SEMICOLON'''
    pass


def p_expression_stmt_2(p):
    'expression_stmt : SEMICOLON'
    pass


def p_expression_stmt_3(p):
    '''expression_stmt : COUT LGREATER QUOTES ID QUOTES SEMICOLON
    | COUT LGREATER QUOTES ID QUOTES LGREATER ENDL SEMICOLON
    | COUT LGREATER STRING  SEMICOLON
    | COUT LGREATER STRING  LGREATER ENDL SEMICOLON
    | COUT LGREATER var SEMICOLON
    | COUT LGREATER var LGREATER   ENDL SEMICOLON
    | COUT LGREATER var  LGREATER var SEMICOLON
    | COUT LGREATER var LGREATER  var LGREATER ENDL SEMICOLON
    '''
    pass


def p_expression_stmt_4(p):
    '''expression_stmt : CIN RGREATER var SEMICOLON
    | CIN RGREATER var  RGREATER var SEMICOLON
    | CIN POINT GET LPAREN RPAREN SEMICOLON
    '''
    pass


def p_expression_stmt_5(p):
    '''expression_stmt : ID PLUSPLUS
    | PLUSPLUS ID
    | ID MINUSMINUS
    | MINUSMINUS ID
    '''
    pass


def p_selection_stmt_1(p):
    'selection_stmt : IF LPAREN expression RPAREN statement'
    pass


def p_selection_stmt_2(p):
    'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
    pass


def p_iteration_stmt(p):
    'iteration_stmt : WHILE LPAREN expression RPAREN statement'
    pass


def p_iteration_stmt1(p):
    '''iteration_stmt :
    | FOR LPAREN type_specifier expression SEMICOLON expression SEMICOLON expression RPAREN statement
    | FOR LPAREN type_specifier expression SEMICOLON expression SEMICOLON var PLUSPLUS RPAREN statement
    | FOR LPAREN type_specifier expression SEMICOLON expression SEMICOLON PLUSPLUS var  RPAREN statement
    | FOR LPAREN type_specifier expression SEMICOLON expression SEMICOLON var MINUSMINUS RPAREN statement
    | FOR LPAREN type_specifier expression SEMICOLON expression SEMICOLON MINUSMINUS var  RPAREN statement
    '''
    pass


def p_return_stmt_1(p):
    'return_stmt : RETURN SEMICOLON'
    pass


def p_return_stmt_2(p):
    'return_stmt : RETURN expression SEMICOLON'
    pass


def p_expression_1(p):
    '''expression : var EQUAL expression'''
    pass


def p_expression_2(p):
    'expression : simple_expression'
    pass


def sintax(t):
    os.system("g++ -Wall "+t)
    pass


def p_var_1(p):
    'var : ID'
    pass


def p_var_2(p):
    'var : ID LBRACKET expression RBRACKET'
    pass


def p_simple_expression_1(p):
    'simple_expression : additive_expression relop additive_expression'
    pass


def p_simple_expression_2(p):
    'simple_expression : additive_expression'
    pass


def p_relop(p):
    '''relop : LESS
        | LESSEQUAL
        | GREATER
        | GREATEREQUAL
        | DEQUAL
        | DISTINT
        | QUOTES
    '''
    pass


def p_additive_expression_1(p):
    'additive_expression : additive_expression addop term'
    pass


def p_additive_expression_2(p):
    'additive_expression : term'
    pass


def p_addop(p):
    '''addop : PLUS
    | MINUS
    '''
    pass


def p_term_1(p):
    'term : term mulop factor'
    pass


def p_term_2(p):
    'term : factor'
    pass


def p_mulop(p):
    '''mulop : 	TIMES
                | DIVIDE
    '''
    pass


def p_factor_1(p):
    'factor : LPAREN expression RPAREN'
    pass


def p_factor_2(p):
    'factor : var'
    pass


def p_factor_3(p):
    'factor : call'
    pass


def p_factor_4(p):
    'factor : NUMBER'
    pass


def p_call(p):
    'call : ID LPAREN args RPAREN'
    pass


def p_args(p):
    '''args : args_list
            | empty
    '''
    pass


def p_args_list_1(p):
    'args_list : args_list COMMA expression'
    pass


def p_args_list_2(p):
    'args_list : expression'
    pass


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Error de sintaxis",p)
    print ("Error en la linea "+ str(p.lineno))

#Traducir el resultado del test
#def traducir(result):
#	graphFile = open('graphviztrhee.vz','w')
#	graphFile.write(result.traducir())
#	graphFile.close()
#	print ("El programa traducido se guardo en \"graphviztrhee.vz\"")

parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'C:/Users/zurie/Desktop/CompiladorC/test1.cpp'

    f = open(fin,'r')
    data = f.read()
    print (data)
    parser.parse(data, tracking=True)
    sintax(fin)


