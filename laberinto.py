# Isai Aleman Calderon

import re
import math
import Nodo 
import Arco
import Grafo

archivo = open("laberinto.csv")
# linea   = linea.rstrip()
# linea   = linea.strip()
lineas = archivo.readlines()
n = len(lineas)
A = []
print("Lineas: ", n)
for linea in lineas:
	linea = linea.rstrip()
	linea = linea.strip()
	linea = linea.split('-')
	A.append(linea)
# print(A)
col = len(linea)  # 28
row = len(lineas) # 21
nodos = []

for y in  range(row):
	for x in range(col):
		tmp = []
		
		node = str((x+1)) +","+ str(y+1)
		# print("Iteracion: "+node)
		
		tmp.append(node)
		# print(A[y][x])
		char = A[y][x]
		# print(char)
		if  char == str(1):
			# print("Hay 1")
			if x < (col-1):
				if A[y][x+1] == str(1):
					# print("Tengo un 1 a mi derecha")
					node = str((x+2)) +","+ str(y+1)
					tmp.append(node)
			if x > 0:
				if A[y][x-1] == str(1):
					# print("Tengo un 1 a mi izquierda")
					node = str((x)) +","+ str(y+1)
					tmp.append(node)
					
			if y < (row-1):
				if A[y+1][x] == str(1):
					# print("Tengo un 1 a mi abajo")
					node = str((x+1)) +","+ str(y+2)
					tmp.append(node)
					
			if y > 0:
				if A[y-1][x] == str(1):
					# print("Tengo un 1 a mi arriba")
					node = str((x+1)) +","+ str(y)
					tmp.append(node)
					
			# print("llege al limite en la col: ", col)
		
			# print("Valor x+1: ", A[y][x+1], "en "+node)
		nodos.append(tmp)
	# print("")

# print(nodos, sep=" --")
for nodo in nodos:
	print(nodo)
archivo.close()