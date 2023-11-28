# -*- enconding: utf-8 -*-
import os
import ctypes
import tkinter as tk
import tkinter.filedialog
from time import sleep

def Analizador_sintactico(rutaCPP):
	ftypes = [('Archivos de C++', '*.cpp')]
	dlg = tk.filedialog.Open(filetypes= ftypes, title = "Abrir codigo c++")
	fl = dlg.show()
	a=fl
	wd=os.getcwd()
	#print("directorio actual ",wd)
	b = wd.replace("\\","/")
	#print("directorio remplazado ",b)
	if (os.path.exists(a)):
		os.system(rutaCPP + "g++ "+ a + " -o "+ b +"/salida.o")
		if (os.path.exists(b + "/salida.o")):
			os.system("del " + wd +"\\salida.o")
			ctypes.windll.user32.MessageBoxW(0, "El codigo esta perfecto","Analizador sintactico",1)
			os.system("notepad.exe "+ b +"/COM/parser.out")
		else:
			ctypes.windll.user32.MessageBoxW(0,"El codigo presenta errores de Sintaxis","Analizador Sintactico",1)
	else:
		print ("Error  en el nombre del archivo")

def OBJ(rutaCPP):
	ftypes=[('Archivos de C++', '*.cpp')]
	dlg = tk.filedialog.Open(filetypes= ftypes, title = "Abrir codigo de c++")
	fl = dlg.show()
	a=fl
	wd=os.getcwd()
	b = wd.replace("\\","/")
	if(os.path.exists(a)):
		ftypes = [('Codigo de Objeto', '*.o')]
		filename = tk.filedialog.asksaveasfilename(title = "Donde guardar el codigo")
		ss = filename.replace("/","\\")		
		os.system(rutaCPP + "g++ " + a + " -o " + ss)
		#sleep(5000)
		ss = filename.replace("\\","/")
		if (os.path.exists(ss)):
			ctypes.windll.user32.MessageBoxW(0, "El archivo fue creado exitosamente","Archivo Objeto",1)
		else:
			ctypes.windll.user32.MessageBoxW(0,"El codigo presenta errores de sintaxis","Archivo Objeto",1)
			os.system("cmd /k"+ rutaCPP + "g++ " + a + " -o "+ b +"/salida.o")

def EXE(rutaCPP):
	ftypes=[('Archivos de C++', '*.cpp')]
	dlg = tk.filedialog.Open(filetypes= ftypes, title = "Abrir codigo de c++")
	fl = dlg.show()
	a=fl
	wd=os.getcwd()
	b = wd.replace("\\","/")
	if(os.path.exists(a)):
		ftypes = [('Programa compilado', '*.exe')]
		filename = tk.filedialog.asksaveasfilename(title = "Donde guardar el codigo")
		ss = filename.replace("/","\\")		
		os.system(rutaCPP + "g++ " + a + " -o " + ss)
		#print(rutaCPP + "g++ -Wall -c " + a + " -o " + ss)
		if (os.path.exists(ss)):
			ctypes.windll.user32.MessageBoxW(0, "El programa fue compilado con exito","Archivo exe",1)
		else:
			ctypes.windll.user32.MessageBoxW(0,"El codigo presenta errores de sintaxis","Archivo Exe",1)
			os.system("cmd /k"+ rutaCPP + "g++ " + a + " -o "+b +"/salida.o")

def RUN():
	ftypes=[('Archivos compilados', '*.exe')]
	dlg = tk.filedialog.Open(filetypes= ftypes, title = "Abrir archivo compilado")
	fl = dlg.show()
	a= fl.replace("/","\\")	
	os.system(a)
