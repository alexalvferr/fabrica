from tkinter import *
root = Tk()
root.geometry("700x200")
root.resizable(0,0)
root.configure(bg="#c3e8de")
root.title("Calculadora")

def limpar():
    numero1_entrada.delete(0, END)
    numero2_entrada.delete(0, END)

def soma():
    n1 =numero1.get()
    n2 = numero2.get()
    res = n1 + n2
    vresultado.set(res)

def sub():
    n1 =numero1.get()
    n2 = numero2.get()
    res = n1 - n2
    vresultado.set(res)

def mulp():
    n1 =numero1.get()
    n2 = numero2.get()
    res = n1*n2
    vresultado.set(res)

def divisao():
    n1 =numero1.get()
    n2 = numero2.get()
    res = n1/n2
    resarr = round(res,2)
    vresultado.set(resarr)



numero1 = DoubleVar()
numero2 = DoubleVar()
vnumero1 = Label(text="Número 1:",bg="#c3e8de",fg="#6d7062",font=("Arial","14","bold"))
vnumero1.place(relx=0.05,rely=0.3)
numero1_entrada= Entry(textvariable=numero1,font=("Arial","12","bold"),bg="white",fg="red",justify='center')
numero1_entrada.place(relx=0.2,rely=0.3,relwidth=0.1)

vnumero2 = Label(text="Número 2:",bg="#c3e8de",fg="#6d7062",font=("Arial","14","bold"))
vnumero2.place(relx=0.32,rely=0.3)
numero2_entrada= Entry(textvariable=numero2,font=("Arial","12","bold"),bg="white",fg="red",justify='center')
numero2_entrada.place(relx=0.48,rely=0.3,relwidth=0.1)

butlimpar = Button( text="Limpar", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'), command=limpar)
butlimpar.place(relx=0.05, rely=0.6, relwidth=0.15, relheight=0.15)
butsoma = Button( text="+", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'),command=soma)
butsoma.place(relx=0.45, rely=0.6, relwidth=0.1, relheight=0.15)
butsub = Button( text="-", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'),command=sub)
butsub.place(relx=0.6, rely=0.6, relwidth=0.1, relheight=0.15)
butmult = Button( text="*", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'),command=mulp)
butmult.place(relx=0.72, rely=0.6, relwidth=0.1, relheight=0.15)
butdiv = Button( text="/", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'),command=divisao)
butdiv.place(relx=0.85, rely=0.6, relwidth=0.1, relheight=0.15)

texto1 = Label(text="Resultado:",bg="#c3e8de",fg="#6d7062",font=("Arial","14","bold"))
texto1.place(relx=0.6,rely=0.3)
vresultado = StringVar()
resultado=Label( textvariable=vresultado,bg="#c1d5ee",
                 font=('verdana', 14, 'bold'))
resultado.place(relx=0.75,rely=0.3,relwidth=0.2)
root.mainloop()
