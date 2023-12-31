# -*- enconding: utf-8 -*-
import ply.lex as lex
import tkinter as tk
import tkinter.filedialog
import os , re ,sys , codecs

#lista de tokens

tokens = (

	#Palabras Reservadas
	'INCLUDE',
	'USING',
	'NAMESPACE',
	'STD',
	'COUT',
	'CIN',
	'GET',
	'ENDL',
	'ELSE',
	'IF',
	'INT',
	'STRING',
	'RETURN',
	'VOID',
	'WHILE',
	'FOR',

	#SYMBOLOS
	'HASH',
	'POINT',
	'PLUS',
	'PLUSPLUS',
	'MINUS',
	'MINUSMINUS',
	'TIMES',
	'DIVIDE',
	'LESS',
	'LESSEQUAL',
	'GREATER',
	'GREATEREQUAL',
	'EQUAL',
	'DEQUAL',
	'DISTINT',
	'SEMICOLON',
	'COMMA',
	'LGREATER',
	'RGREATER',
	'LPAREN',
	'RPAREN',
	'LBRACKET',
	'RBRACKET',
	'LBLOCK',
	'RBLOCK',
	'QUOTES',

	#MISC
	'ID',
	'NUMBER',

)

#EXPRESIONES REGULARES PARA TOKENS DE CONTEXTO SIMPLE

t_PLUS = r'\+'
t_MINUS = r'-'
t_MINUSMINUS = r'\-\-'
t_POINT = r'\.'
r_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_QUOTES = r'\"'

def t_INCLUDE(t):
	r'include'
	return t

def t_USING(t):
	r'using'
	return t

def t_NAMESPACE(t):
	r'namespace'
	return t

def t_STD(t):
	r'std'
	return t

def t_COUT(t):
	r'cout'
	return t

def t_CIN(t):
	r'cin'
	return t

def t_GET(t):
	r'get'
	return t

def t_ENDL(t):
	r'endl'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_IF(t):
	r'if'
	return t

def t_INT(t):
	r'int'
	return t

def t_RETURN(t):
	r'return'
	return t

def t_VOID(t):
	r'void'
	return t

def t_WHILE(t):
    r'while'
    return t


def t_FOR(t):
    r'for'
    return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

#expresion regular para identificadores

def t_ID(t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value.upper() in tokens:
                t.value = t.value.upper()
                t.type = t.value
        return t

def t_STRING(t):
	r'\"?(\w + \ * \w*\d* \ *)\"?'
	return t		

def t_HASH(t):
	r'\#'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEQUAL(t):
	r'>='
	return t

def t_dEQUAL(t):
	r'=='
	return t

def t_LGREATER(t):
	r'<<'
	return t	

def t_RGREATER(t):
	r'>>'
	return t

def t_DISTINT(t):
	r'!='
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
	r'//(.)*?\n'
	t.lexer.lineno += 1

def t_error(t):
	print (("Error Lexico: "+ str(t.value[0])))
	t.lexer.skip(1)


def test(data, lexer):
	lexer.input(data)
	f=open('C:/Users/zurie/Desktop/CompiladorC/Salida.txt','w')
	f.write("")
	while True:
		tok = lexer.token()
		if not tok:
			break
		f = open('C:/Users/zurie/Desktop/CompiladorC/Salida.txt','a')
		f.write(str(tok)+ "\n")
		
		#print (tok)
	os.system("notepad.exe C:/Users/zurie/Desktop/CompiladorC/Salida.txt")
lexer = lex.lex()

def Analizador_Lexico():
	ftypes=[('Archivos de C++','*.cpp'),('Todos los Archivos','*')]
	dlg = tk.filedialog.Open( filetypes = ftypes )
	fl = dlg.show()
	a = fl
	if (os.path.exists (a)):
		f = open(a)
		data = f.read()
		f.close()
		#contruir lexer y probarlo
		lexer.input(data)
		test(data,lexer)
	else:
		print("El archivo no existe")             


#testeo
if __name__ == '__main__':

    # Test  ESTO ES SOLO PARA PROBAR EL FUNCINAMIENTO DE ANIZADOR LEXICO.
    #Cargamos el archivo "test1.cpp" que esta en la carpeta ejemplos y lo guardamos
    #la variable data para despues enviarla al analizador lexico para que la descomponga en tokes

    f = open('C:/Users/zurie/Desktop/CompiladorC/test1.cpp')
    data = f.read()
    f.close()
    #Creamos el lexer y lo comprobamos
    lexer.input(data)
    test(data, lexer)

#for x in range(0,len(cadena)):
#    resultado=contador_caracteres(cadena[x])
#    print('El Token '+ cadena[x] +' contine '+ str(resultado)+ ' caracteres ')
#    token += 1
#    rtotal+= resultado

#print('Por lo que el lexema '+texto+' contiene un total de: ')     
#print(str(token)+' tokens y '+ str(rtotal)+' caracteres')

#msvcrt.getch()
