import tkinter as tk
import tkinter.filedialog
from COM.c_lexer import Analizador_Lexico
import ply.armar as construir
import sys, os, string 
rutaCPP=""
class Example(tk.Frame):

	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
                
		#submit0= tk.Label(self,text="Compilador de C++",bg="cyan")
		submit1= tk.Button(self,text="Programa fuente",command=self.boton1)
		submit2= tk.Button(self,text="Analizador Lexico",command=self.boton2)
		submit3= tk.Button(self,text="Analizador Sintactico",command=self.boton3)
		submit4= tk.Button(self,text="Convertir a Codigo Objeto (.O)",command=self.boton4)
		submit5= tk.Button(self,text="Convertira a Codigo EXE (.BIN)",command=self.boton5)
		submit6= tk.Button(self,text="Ejecutar programa",command=self.boton6)
		submit7= tk.Button(self,text="Readme",command=self.boton7)

		#submit0.pack(side="top",fill="x", expand=True)
		submit1.pack(side="top",fill="x", expand=True)
		submit2.pack(side="top",fill="x", expand=True)
		submit3.pack(side="top",fill="x", expand=True)
		submit4.pack(side="top",fill="x", expand=True)
		submit5.pack(side="top",fill="x", expand=True)
		submit6.pack(side="top",fill="x", expand=True)
		submit7.pack(side="top",fill="x", expand=True)

	def boton1(self):
		ftypes = [('Archivos de c++.','*.cpp')]	
		dlg = tk.filedialog.Open( filetypes=ftypes,title = "Abrir codigo de c++")
		fl = dlg.show()
		os.system("notepad.exe "+ fl)

	def boton2(self):
		Analizador_Lexico()

	def boton3(self):
		global rutaCPP
		construir.Analizador_sintactico(rutaCPP);

	def boton4(self):
		global rutaCPP
		construir.OBJ(rutaCPP)

	def boton5(self):
		global rutaCPP	
		construir.EXE(rutaCPP)

	def boton6(self):
		construir.RUN()

	def boton7(self):
                os.system("notepad.exe info.txt")

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("400x250")
	root.title("Compilador de C++")
	root.iconbitmap("c++.ico")
	Example(root).pack(fill="both", expand=True)
	root.mainloop()
