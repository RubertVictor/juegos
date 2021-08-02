# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:06:02 2017

@author: victor
"""
import tkinter
import random


class appBuscaminas():
    def __init__(self):
        self.i=15
        self.j=15
        
        self.vacios=[] #Array con los numeros (las coordenadas) de las celdas vacias
        self.num_desv=[] #Array con los numeros (las coordenadas) que ya se han mostrado al usuario
        self.casillas=self.i*self.j
        self.crear_bombas()
        self.array=[0]*self.i # Matriz de botones
        for a in range(self.i):
            self.array[a]=[0]*self.j
        
        self.ventana =tkinter.Tk() 
        #self.ventana.iconbitmap('C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\icono.ico')
        self.ventana.title("Buscaminas")        
        
        self.bomroja=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\bombaroja.gif')
        self.bom=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\bomba.gif')
        self.uno=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\uno.gif')
        self.dos=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\dos.gif')
        self.tres=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\tres.gif')
        self.cautro=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\cuatro.gif')
        self.cinco=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\cinco.gif')
        self.seis=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\seis.gif')
        self.siete=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\siete.gif')
        self.ocho=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\ocho.gif')
        self.gris=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\gris.gif')
        self.cara1=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\cara1.gif')
        self.cara2=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\cara2.gif')
        self.cara3=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\cara3.gif')
        self.cara4=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\cara4.gif')
        self.flag=tkinter.PhotoImage(file='C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\bandera.gif')
        
        self.bdh=tkinter.Menu(self.ventana)
        self.juego=tkinter.Menu(self.bdh,tearoff=False)

        
        self.bdh.add_cascade(label="Juego",menu=self.juego)

               
        self.juego.add_command(label="Nuevo Juego",command=self.reset)
        self.juego.add_command(label="Configuracion",command=self.configuracion)

        
        
        self.ventana.config(menu=self.bdh)
        
        
        self.top=tkinter.Frame(self.ventana,relief="ridge",borderwidth=2,height=35)
        self.top.pack(fill="both")
        
        self.atras=tkinter.Frame(self.ventana)
        self.atras.pack()
        
        
        self.carita=tkinter.Button(self.top,image=self.cara1,command=self.reset,height=20,width=20)
        self.carita.bind(sequence="<Enter>",func=self.carita2)
        self.carita.pack()
        for a in range(self.i):
            for b in range(self.j):
                self.array[a][b]=tkinter.Button(self.atras,height=13,width=13,padx=0,pady=0,image=self.gris)
                self.comando(a,b)
                self.comando2(a,b)
                self.array[a][b].grid(row=a,column=b)
        
        
        self.ventana.mainloop()


    
    def cambiar(self):
        
        if(int(self.base.get())<73):
            self.j=int(self.base.get())
        if(int(self.altura.get())<35):
            self.i=int(self.altura.get())
        self.conf.destroy()
        self.reset()
        
        
        
    def configuracion(self):
        
        self.conf=tkinter.Tk()
        self.conf.title("Configuración")  
        self.conf.iconbitmap('C:\\users\\victo\\Escritorio\\Programacio\\Personal\\IA\\juegos\\buscaminas\\icono.ico')
        self.L1=tkinter.Label(self.conf,text="Base")
        self.L2=tkinter.Label(self.conf,text="Altura")
        self.base=tkinter.Entry(self.conf,text="Base")
        self.altura=tkinter.Entry(self.conf,text="Altura")
        self.aceptar=tkinter.Button(self.conf,command=self.cambiar,text="Aceptar")
    
        
        self.L1.grid(row=1,column=0)
        self.L2.grid(row=2,column=0)
        self.base.grid(row=1,column=1)
        self.altura.grid(row=2,column=1)
        self.aceptar.grid(row=3,column=0)
        self.conf.mainloop()
    
    def carita2(self,event):
        self.carita.config(image=self.cara2)
        
    def nada(self):
        pass
        
    def comando(self,a,b):
        
        self.array[a][b].config(command=lambda: self.desvelar(a,b))
    
    def comando2(self,a,b):
        self.array[a][b].bind(sequence="<Button-3>",func=self.bandera)
    
    def gameover(self):
        for a in range(self.i):
            for b in range(self.j):
                if(self.bombas[a+1][b+1]==-1):
                    self.array[a][b].config(image=self.bom,relief="flat")
                    self.bombas[a+1][b+1]=18
                elif(not [a,b] in self.vacios):
                    
                    self.array[a][b].config(command=self.nada)
        self.carita.config(image=self.cara4)
    
    def vacio(self,a,b):
        if(not [a,b] in self.vacios):
            self.vacios.append([a,b])   
            self.array[a][b].destroy()
        
        for c in self.vacios:
    
            for d in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                if (self.bombas[c[0]+d[0]+1][c[1]+d[1]+1]==0 and not [c[0]+d[0],c[1]+d[1]] in self.vacios ):
                    self.vacios.append([c[0]+d[0],c[1]+d[1]])
                    self.array[c[0]+d[0]][c[1]+d[1]].destroy()
                    
    
    
                elif(self.bombas[c[0]+d[0]+1][c[1]+d[1]+1]!=-3 and self.bombas[c[0]+d[0]+1][c[1]+d[1]+1]!=0 and not ([c[0]+d[0],c[1]+d[1]] in self.num_desv)):
                    
                    self.num_desv.append([c[0]+d[0],c[1]+d[1]])
                    self.desvelar(c[0]+d[0],c[1]+d[1])
                    
    def desvelar(self,posa,posb):
        
        if (self.bombas[posa+1][posb+1]==-1):
            self.array[posa][posb].config(image=self.bomroja,relief="flat")
            self.bombas[posa+1][posb+1]=-2
            self.gameover()
            
        elif(self.bombas[posa+1][posb+1]==0):
            self.vacio(posa,posb)
        
        elif (self.bombas[posa+1][posb+1]==1):
            self.array[posa][posb].config(image=self.uno,relief="flat")
            self.bombas[posa+1][posb+1]=18
            if(not [posa,posb] in self.num_desv):
                self.num_desv.append([posa,posb])
            
            
        elif (self.bombas[posa+1][posb+1]==2):
            self.array[posa][posb].config(image=self.dos,relief="flat")
            self.bombas[posa+1][posb+1]=18
            if(not [posa,posb] in self.num_desv):
                self.num_desv.append([posa,posb])
            
        elif (self.bombas[posa+1][posb+1]==3):
            self.array[posa][posb].config(image=self.tres,relief="flat")
            self.bombas[posa+1][posb+1]=18
            if(not [posa,posb] in self.num_desv):
                self.num_desv.append([posa,posb])
            
        elif (self.bombas[posa+1][posb+1]==4):
            self.array[posa][posb].config(image=self.cautro,relief="flat")
            self.bombas[posa+1][posb+1]=18
            if(not [posa,posb] in self.num_desv):
                self.num_desv.append([posa,posb])
            
        elif (self.bombas[posa+1][posb+1]==5):
            self.array[posa][posb].config(image=self.cinco,relief="flat")
            self.bombas[posa+1][posb+1]=18
            if(not [posa,posb] in self.num_desv):
                self.num_desv.append([posa,posb])
            
        elif (self.bombas[posa+1][posb+1]==6):
            self.array[posa][posb].config(image=self.seis,relief="flat")
            self.bombas[posa+1][posb+1]=18
            if(not [posa,posb] in self.num_desv):
                self.num_desv.append([posa,posb])
            
        elif (self.bombas[posa+1][posb+1]==7):
            self.array[posa][posb].config(image=self.siete,relief="flat")
            self.bombas[posa+1][posb+1]=18
            if(not [posa,posb] in self.num_desv):
                self.num_desv.append([posa,posb])
            
        elif (self.bombas[posa+1][posb+1]==8):
            self.array[posa][posb].config(image=self.ocho,relief="flat")
            self.bombas[posa+1][posb+1]=18
            if(not [posa,posb] in self.num_desv):
                self.num_desv.append([posa,posb])
            
    
        if((self.casillas-((len(self.vacios))+len(self.num_desv)))==self.num_bombas):
            self.carita.config(image=self.cara3)
         
    def bandera(self,evento):
        for a in range(len(self.array)):
            if (evento.widget in self.array[a]):
                for b in range(len(self.array[0])):
                    if (self.array[a][b]==evento.widget):
                        
                        if(self.bombas[a+1][b+1]>-2 and self.bombas[a+1][b+1]<9):
                            self.bombas[a+1][b+1]+=11
                            evento.widget.config(image=self.flag)
                            
                        elif(self.bombas[a+1][b+1]>8 and self.bombas[a+1][b+1]<18):
                            self.bombas[a+1][b+1]-=11
                            evento.widget.config(image=self.gris)
    
    
    def reset(self):
        self.vacios=[]
        self.casillas=self.i*self.j
        self.num_desv=[]
        self.crear_bombas()
        for a in range(len(self.array)):
            for b in range(len(self.array[0])):
                self.array[a][b].destroy()
        self.array=[0]*self.i # Matriz de botones
        for a in range(self.i):
            self.array[a]=[0]*self.j    
        for a in range(self.i):
            for b in range(self.j):
                self.array[a][b]=tkinter.Button(self.atras,height=13,width=13,padx=0,pady=0,image=self.gris)
                self.comando(a,b)
                self.comando2(a,b)
                self.array[a][b].grid(row=a,column=b)
        self.carita.config(image=self.cara1)
    
    
    
    #Colocamos las bombas de forma aleatoria--------------------------------------------
    def crear_bombas(self):
        self.num_bombas=0
        self.bombas=[-3]*(self.i+2)
        for a in range (self.i+2):
            self.bombas[a]=[-3]*(self.j+2)#Colocamos -3 en las orillas
            
        for a in range(1,self.i+1):
            for b in range(1,self.j+1):
                self.bombas[a][b]=0 #Colocamos 0 en el centro
        for a in range(1,self.i+1):
            for b in range(1,self.j+1):
                if(random.randint(0,5)==0):
                    self.bombas[a][b]=-1 #Ponemos las bombas
                    self.num_bombas+=1
        for a in range(1,self.i+1):
                for b in range(1,self.j+1):
                        for d in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                            if(self.bombas[a][b]!=-1 and self.bombas[a+d[0]][b+d[1]]==-1):
                                self.bombas[a][b]+=1 #Ponemos los numeros

if (__name__=="__main__"):
    appBuscaminas()





