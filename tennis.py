# -*- coding: utf8 -*-

"""
	SIMULANDO UN JUEGO DE TENNIS
	>>> mostrar_score()
	'[0-0]'
	>>> anotar(1,0)
	'[advantage-0]'
	>>> mostrar_score()
	'[15-0]'
	>>> anotar(1,0)
	'[advantage-0]'
	>>> mostrar_score()
	'[30-0]'
	>>> anotar(1,0)
	'[advantage-0]'
	>>> mostrar_score()
	'[40-0]'
	>>> anotar(1,0)
	'[set-0]'
	>>> mostrar_score()
	'[50-0]'
	
"""
player1 = 0
player2 = 0
vuelta1 = 0
vuelta2 = 0
puntos1 = 0
puntos2 = 0
extra1 = 0
extra2 = 0

def mostrar_score():
	print "["+str(player1)+"-"+str(player2)+"]"

def anotar(play1, play2):
	info = ""
	global player1,player2,vuelta1,vuelta2,puntos1,puntos2,extra1,extra2
	
	if vuelta1 <= 1:
		puntos1 = 15
	if vuelta2 <= 1:
		puntos2 = 15
	if vuelta1 >= 2:
		puntos1 = 10
	if vuelta2 >=2:
		puntos2 = 10
		
	if play1 == 1: #Anoto el jugador 1
		player1 += puntos1
		vuelta1 += 1
	elif play2 == 1: #Anoto el jugador 2
		player2 += puntos2
		vuelta2 += 1
	
	
	if player1 == player2:
		print 'deuse'
	elif player1 > player2:
		print "[advantage-"+str(player2)+"]"
	elif player1 < player2:
		print "["+str(player1)+"-advantage]"
	if player1 >= 40:
		extra1 += 1
		extra2 = 0
	if player2 >= 40:
		extra2 += 1
		extra1 = 0
	#VALIDAR SI GANO DOS VECES SEGUIDAS
	if extra1 == 2:
		print "[set-"+str(player2)+"]"
	elif extra2 == 2:
		print "["+str(player1)+"-set]"


	
	
	
	
	
		
