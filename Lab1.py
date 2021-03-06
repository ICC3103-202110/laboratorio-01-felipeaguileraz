#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:40:25 2021

@author: pipo
"""
import numpy as np
import random

n_cards = int(input("Cuantas cartas quieres jugar? "))
p_player1 = 0  #puntos jugador1
p_player2 = 0  #puntos jugador 2
player = 1     #jugador que esta jugando
list1 = []


for i in range(n_cards):
    n = i+1
    list1.append(n)   #se añade doble ya que son pares
    list1.append(n)
    
random.shuffle(list1)

lengthBoard = n_cards #ancho del tablero
board = []    

def create_board():
    for i in range(2): #se usa 2, para que así funcione el tablero
        line_board = []
        for j in range(lengthBoard):
            line_board.append((i,j))        
        board.append(line_board)     
        
def print_board():
    for i in board:   #for para lineas
        for j in i:   #for para columnas
            print(j, end=" ")
        print()  #cambiar de linea
    print()


      
game = 0
create_board()
print_board()

number_matrix=[]  #se crea la matriz en la que van a ir los numeros para el tablero
nm = 0
for i in range (2):
    number_matrix.append([])
    for j in range(n_cards):
            number_matrix[i].append(list1[nm])
            nm = nm+1
    
while game == 0:  #ciclo en el cual se esta jugando el juego
    print("Turno del jugador: ", player)
    turn1 = 0
    turn2 = 0
    if turn1 == 0:
        y1 = int(input("coordenada y del numero: "))
        x1 = int(input("coordenada x del numero: "))
        turn1 = 1
    print("Tu numero es: ", number_matrix[y1][x1])
    
    board[y1][x1] = number_matrix[y1][x1]  #imprime la matriz con el numero obtenido
    for i in board:
        for j in i:
          print(j, end=" ")  
        print()
    
    if turn2 == 0:
        y2 = int(input("coordenada y del segundo numero: "))
        x2 = int(input("coordenada x del segundo numero: "))
        turn2 = 1
    print("Tu segundo numero es: ", number_matrix[y2][x2])
    
    board[y2][x2] = number_matrix[y2][x2]
    for i in board:
        for j in i:
          print(j, end=" ")  
        print()
    
    if number_matrix[y1][x1] == number_matrix[y2][x2]:  #corrobora que el jugador haya sacado el mismo numero
        print()
        print("Ganaste un punto")
        print()
        if player == 1:
           p_player1 += 1
        else:
            p_player2 += 1
    else:
        print()
        board[y1][x1] = (y1,x1)  #llena el tablero con la tupla de las coordenadas que escogio el jugador
        board[y2][x2] = (y2,x2)
        print_board()
        if player == 1:
            player = 2
        else:
            player = 1
    
        

    
    
    

      

