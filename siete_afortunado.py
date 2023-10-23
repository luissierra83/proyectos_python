from tkinter import *
import random


class SieteAfortunado:
    def __init__(self):
        self.crear_interfaz()
    
    def crear_interfaz(self):
        ventana = Tk()
        ventana.minsize(340,450)
        ventana.geometry('340x450')

        boton = Button(ventana,text="Jugar!", command=self.jugar,font='arial 18 bold')#elementos para construir un boton XD
        boton.pack()

        foto = PhotoImage(file=r'dinero.png')
        foto = foto.subsample(15) #con .zoom le subimos al tamaño y con .subsample lo reducimos
        self.gano=Label(ventana, image=foto)

        self.campos = [StringVar() for elemento in range (3)]
        posicion = 10
        for campo in self.campos:
            label = Label(ventana,textvariable=campo,background='White',foreground='Black',font='arial 42 bold')
            label.place(x=posicion,y=100,width=100,height=100)
            posicion += 110
        mainloop()
    def generar_numero(self):
        return random.randint(0,9)
    def jugar(self):   #aqui está la lógica del juego
        hay_siete = False
        for i in range (3):
            valor = self.generar_numero() #definimos la variable valor
            self.campos[i].set(valor)# agregamos el valor a campos
            if (valor == 7):
                hay_siete = True  #determinamos si ha siete o no
        
        if(hay_siete):
            self.gano.pack(side=BOTTOM)
        else:
            self.gano.pack_forget()

jugar=SieteAfortunado()