# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:06:02 2017

@author: victor
"""
from classeMatriu2 import Matriu
import tkinter
import random
import math
import time
class app2048():
    def __init__(self):
        self.colores=["#eeeeee","#f6e2c4","#f6c170","#fb9f52","#ff6842","#fd4c00","#e5dd24","#e5dd24","#eccd16","#eccd16","#f6d300"]
        self.ventana=tkinter.Tk()
        self.ventana.title("Juego 2048")
        self.ventana.iconbitmap('C:\\Users\\victo\\Escritorio\\Programacio\\Personal\\Projectes\\juegos\\2048\\icono.ico')
        self.puntos=0
        self.fondo=tkinter.Canvas(self.ventana,height=302,width=302,bg="#7e7e7e")#Es color gris clar es #b0afaf
        self.fondo.pack()
        for c in range(4):
            for d in range(4):
                self.fondo.create_rectangle(5+d*75,5+c*75,5+d*75+70,5+c*75+70,fill="#b0afaf",outline="#b0afaf")
                self.fondo.update()
        
        self.tablero=Matriu(4,4)
        self.posar_num()
        self.ventana.bind("<Up>",self.arriba)
        self.ventana.bind("<Down>",self.abajo)
        self.ventana.bind("<Left>",self.izquierda)
        self.ventana.bind("<Right>",self.derecha)
        
        self.ventana.mainloop()


    def mostrar(self):
        self.quadricula=[]
        self.fondo.delete("baldosa")
        for a in range(len(self.tablero.dades)):
            for b in range(len(self.tablero.dades[0])):
                if(self.tablero.dades[a][b]!=0):
                    self.quadricula.append([self.fondo.create_rectangle(5+b*75,5+a*75,5+b*75+70,5+a*75+70,fill=self.colores[int((math.log(self.tablero.dades[a][b]))/(math.log(2)))-1],outline=self.colores[int((math.log(self.tablero.dades[a][b]))/(math.log(2)))-1],tag="baldosa")])
                    self.quadricula[-1].append(self.fondo.create_text(40+b*75,40+a*75,text=str(self.tablero.dades[a][b]),font=("Arial","-30","bold"),fill="#454545",tag="baldosa"))       
    def gameover(self):
        print("no hi ha puesto")
    def derecha(self,event):
        if(self.tablero.moure_dreta()):
            sums=self.tablero.deslizar_r()
            for c in sums:
                self.puntos+=self.tablero.dades[c[0]][c[1]]
            self.posar_num()
            self.mostrar()
    def izquierda(self,event):
        if(self.tablero.moure_esquerra()):
            sums=self.tablero.deslizar_l()
            for c in sums:
                self.puntos+=self.tablero.dades[c[0]][c[1]]
            self.posar_num()
            self.mostrar()
            
    def arriba(self,event):
        if(self.tablero.moure_adalt()):
            sums=self.tablero.deslizar_u()
            for c in sums:
                self.puntos+=self.tablero.dades[c[0]][c[1]]
            self.posar_num()
            self.mostrar()    
    def abajo(self,event):
        if(self.tablero.moure_abaix()):
            sums=self.tablero.deslizar_d()
            for c in sums:
                self.puntos+=self.tablero.dades[c[0]][c[1]]
            self.posar_num()
            self.mostrar()
    
    
    def posar_num(self):
        i=random.randint(0,3)
        j=random.randint(0,3)
        if(self.tablero.num_ceros()!=0):
            while(self.tablero.dades[i][j]!=0):
                i=random.randint(0,3)
                j=random.randint(0,3)
            self.mostrar()
            self.tablero.dades[i][j]=2+2*(math.floor(random.randint(0,7)/7))        
            self.fondo.create_rectangle(10+j*75,10+i*75,0+j*75+70,0+i*75+70,fill=self.colores[int((math.log(self.tablero.dades[i][j]))/(math.log(2)))-1],outline=self.colores[int((math.log(self.tablero.dades[i][j]))/(math.log(2)))-1],tag="baldosa")
            self.fondo.create_text(40+j*75,40+i*75,text=str(self.tablero.dades[i][j]),font=("Arial","-30","bold"),fill="#454545",tag="baldosa")
            self.fondo.update()
            time.sleep(0.07)
        if(self.tablero.num_ceros()!=0):
            pass
        else:
            self.gameover()
        self.mostrar()
if __name__=="__main__":
    app2048()

