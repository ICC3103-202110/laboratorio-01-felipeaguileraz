#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:40:25 2021

@author: pipo
"""
import numpy as np
import random

n_cards = int(input("Cuantas cartas quieres jugar? "))
p_player1 = 0
p_player2 = 0
player = 1  
list1 = []
random.shuffle(list1)

for i in range(n_cards):
    n = i+1
    list1.append(n)
    list1.append(n)
    
random.shuffle(list1)

lengthBoard = n_cards #ancho por alto del tablero
board = []    

def create_board():
    for i in range(2): #se usa 2, para que así funcione el tablero
        line = []
        for j in range(lengthBoard):
            line.append((i,j))        
        board.append(line)     
        
def print_board():
    for i in board:   #for para lineas
        for j in i:   #for para columnas
            print(j, end=" ")
        print()  #cambiar de linea
    print()

def change_player(player):
    if player == 1:
        player = 2
    else:
        player = 1

def points(p):
    p += 1
    
    

    
    
    
    
    
  
    
create_board()
print_board()
