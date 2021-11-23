from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


def openNewWindow():    
        def soma():
            var.set(A.get()+ B.get())
            print(var.get()) 
        def Multi():
            var.set(A.get()* B.get())
            print(var.get()) 
        def Div():
            var.set(A.get()/ B.get())
            print(var.get()) 
        def Sub():
            var.set(A.get() - B.get())
            print(var.get()) 
        def Limpar():
            var.set("")
            A.set("")
            B.set("")
            
            
        newWindow = Toplevel(master)
        newWindow.title("Calculadora")
        A = DoubleVar()
        B = DoubleVar()
        var = StringVar()
        ttk.Entry(newWindow,textvariable=A).grid(row=0,column=0)
        ttk.Entry(newWindow,textvariable=B).grid(row=1,column=0)
        ttk.Label(newWindow,textvariable=var).grid(row=0,column=1)
        ttk.Button(newWindow,text ="+",command = soma).grid(row=2,column=0)
        ttk.Button(newWindow,text ="*",command = Multi).grid(row=2,column=1)
        ttk.Button(newWindow,text ="/",command = Div).grid(row=2,column=2)
        ttk.Button(newWindow,text ="-",command = Sub).grid(row=2,column=3)
        ttk.Button(newWindow,text ="C",command = Limpar).grid(row=2,column=4)

def openNewWindowConverter():
        newWindowConverter = Toplevel(master)
        newWindowConverter.title("Converter decimais")
def openNewWindowJokenpo():
        newWindowJokenpo = Toplevel(master)
        newWindowJokenpo.title("Jokenpo")

master = Tk()
label = Label(master,
			text ="Projetos Com Tkinter")

label.pack(pady = 10)
btn = Button(master,
			text ="Calculadora",
			command = openNewWindow)
btn.pack(pady = 10)
btn = Button(master,
			text ="Jokenpo",
			command = openNewWindowJokenpo)
btn.pack(pady = 10)
btn = Button(master,
			text ="Conversor De numeros Decimais",
			command = openNewWindowConverter)
btn.pack(pady = 10)
master.mainloop()
