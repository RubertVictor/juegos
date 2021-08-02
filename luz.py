# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:06:02 2017

@author: victor
"""
import tkinter
import random
import time
from classeMatriu import Matriu

class appLuz():
    def __init__(self):
        self.i=5
        self.j=5
            
        self.ventana=tkinter.Tk()
        self.ventana.title("Apaga la luz")
        
        self.ventana.iconbitmap('C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\apaga_la_luz\\icono.ico')
        
        self.bdh=tkinter.Menu(self.ventana)
        self.juego=tkinter.Menu(self.bdh,tearoff=False)
        
        
        self.bdh.add_cascade(label="Juego",menu=self.juego)
        
        self.juego.add_command(label="Nuevo Juego",command=self.reset)
        self.juego.add_command(label="Configuración",command=self.conf)
        
        self.ventana.config(menu=self.bdh)
        
        self.encendida=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\apaga_la_luz\\luze.gif')
        self.apagada=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\apaga_la_luz\\luza.gif')
        self.inton=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\apaga_la_luz\\interruptoron.gif')
        self.intoff=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\apaga_la_luz\\interruptoroff.gif')
        
        
        
        self.top=tkinter.Frame(self.ventana)
        self.top.pack()
        self.frame=tkinter.Frame(self.ventana)
        self.frame.pack()
        
        self.interruptor=tkinter.Button(self.top,image=self.inton,command=self.switch)
        self.interruptor.grid(row=0,column=0)
        self.cl=tkinter.Label(self.top,text="Clicks:")
        self.cl.grid(row=0,column=1)
        self.num=tkinter.Label(self.top,text="0")
        self.num.grid(row=0,column=2)
        self.on=True
        
        
        self.botons=[0]*self.i
        for a in range(self.i):
            self.botons[a]=[0]*self.j
        self.informacio=Matriu(self.i+2,self.j+2)
        self.zeros=Matriu(self.i,self.j)
        self.clicks=[]
        self.num_clicks=0
        #Cream es botons
        for c in range(self.i):
            for d in range(self.j):
                entrada=tkinter.Button(self.frame,image=self.apagada)
                self.botons[c][d]=entrada
                self.comando(entrada,c,d)
                
                self.botons[c][d].grid(row=c,column=d)
        
        self.reset()
        
        
        
        self.ventana.mainloop()

    def mostrar(self,a,b):
    
        for d in [[-1,0],[0,-1],[0,0],[0,1],[1,0]]:
            if(self.informacio.dades[a+d[0]+1][b+d[1]+1]==0 and 0<a+d[0]+1<self.i+1 and 0<b+d[1]+1<self.j+1):
                self.botons[a+d[0]][b+d[1]].config(image=self.apagada)
            if(self.informacio.dades[a+d[0]+1][b+d[1]+1]==1 and 0<a+d[0]+1<self.i+1 and 0<b+d[1]+1<self.j+1):
                self.botons[a+d[0]][b+d[1]].config(image=self.encendida)
    
    
    def comando(self,boto,a,b,):
        boto.config(command=lambda:self.cambiar(a,b))
    def cambiar(self,a,b):
    
        self.clicks.append([a,b])
        for d in [[-1,0],[0,-1],[0,0],[0,1],[1,0]]:
            if(self.informacio.dades[a+d[0]+1][b+d[1]+1]==0):
                self.informacio.dades[a+d[0]+1][b+d[1]+1]=1
            elif(self.informacio.dades[a+d[0]+1][b+d[1]+1]==1):
                self.informacio.dades[a+d[0]+1][b+d[1]+1]=0
    
        for c in range(self.i):
            for d in range(self.j):
                self.zeros.dades[c][d]=self.informacio.dades[c+1][d+1]
        if(self.zeros.num_ceros()!=self.i*self.j):
            self.num_clicks+=1
        if(self.zeros.num_ceros()==self.i*self.j):
            self.mostrar(a,b)
            for c in range(self.i):
                for d in range(self.j):
                    self.botons[c][d].config(image=self.encendida)
                    self.ventana.update()
                    time.sleep(0.1)
                    self.botons[c][d].config(image=self.apagada)
                    self.ventana.update()
        self.num.config(text=str(self.num_clicks))
        self.mostrar(a,b)
    def reset(self):
        self.clicks=[]
        self.zeros=Matriu(self.i,self.j)
        self.informacio=Matriu(self.i+2,self.j+2)
        for c in range(len(self.botons)):
            for d in range(len(self.botons[0])):
                self.botons[c][d].destroy()
        self.botons=[0]*self.i
        for c in range(len(self.botons)):
            self.botons[c]=[0]*self.j
        for c in range(self.i):
            for d in range(self.j):
                entrada=tkinter.Button(self.frame,image=self.apagada)
                self.botons[c][d]=entrada
                self.comando(entrada,c,d)
            
                self.botons[c][d].grid(row=c,column=d)
        for c in range(self.i):
            for d in range(self.j):
                if(random.randint(1,3)==3):
                    self.botons[c][d].invoke()
        self.num_clicks=0
        self.num.config(text=str(self.num_clicks))
    def switch(self):
        if(self.on):
            self.interruptor.config(image=self.intoff)
            self.zeros=Matriu(self.i,self.j)
            self.informacio=Matriu(self.i+2,self.j+2)
    
            for a in range(self.zeros.files):
                for b in range(self.zeros.columnes):
                    
                    self.mostrar(a,b)
            self.num_clicks=0
            self.num.config(text=str(self.num_clicks))
            self.on=False
        else:
            self.interruptor.config(image=self.inton)
    
            
            self.reset()
            self.on=True
    def conf(self):
        self.confi=tkinter.Tk()
        self.confi.title("Configuración")  
        self.confi.iconbitmap('C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\apaga_la_luz\\icono.ico')
        L1=tkinter.Label(self.confi,text="Base")
        L2=tkinter.Label(self.confi,text="Altura")
        self.base=tkinter.Entry(self.confi,text="Base")
        self.altura=tkinter.Entry(self.confi,text="Altura")
        aceptar=tkinter.Button(self.confi,command=self.dimension,text="Aceptar")
        
            
        L1.grid(row=1,column=0)
        L2.grid(row=2,column=0)
        self.base.grid(row=1,column=1)
        self.altura.grid(row=2,column=1)
        aceptar.grid(row=3,column=0)
        self.confi.mainloop()
    def dimension(self):
        
        self.i=int(self.altura.get())    
        self.j=int(self.base.get())
        self.confi.destroy()
        self.reset()
if __name__=="__main__":        
    appLuz()