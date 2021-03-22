#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:40:25 2021

@author: pipo
"""
import numpy as np

n_cartas = int(input("Cuantas cartas quieres jugar? "))
lista1 = []
lista2 = []
for i in range(n_cartas):
    n = i+1
    lista1.append(n)
    lista2.append(n)

longitudTablero = n_cartas #ancho por alto del tablero
tablero = []    

def crear_tablero():
    for i in range(longitudTablero):
        linea = []
        for j in range(longitudTablero):
            linea.append("*")        
        tablero.append(linea)     
        
def imprimir_tablero():
    for i in tablero:   #for para lineas
        for j in i:   #for para columnas
            print(j, end=" ")
        print()  #cambiar de linea
    print()
            
    
    
    
    
    
    
crear_tablero()
imprimir_tablero()