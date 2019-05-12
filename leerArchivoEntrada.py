#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:22:46 2019

@author: lbeltran
"""
import re
import math
import Nodo 
import Arco
import Grafo 

archivo=open("entrada3.txt")
costo="X"
G = Grafo.Grafo()
linea = archivo.readline()
linea= linea.rstrip()
linea= linea.strip()
tmp= re.findall("^costo\s*=\s*(\S+)",linea)
if(len(tmp)>0):
    costo=tmp[0]
if(costo=="no"):
    for linea in archivo.readlines():
        linea= linea.rstrip()
        linea= linea.strip()
        tmp=re.findall("\S+",linea)
        if(len(tmp)>0):
            origen = G.addNodo(tmp[0])
            for i in range(1,len(tmp)):
                destino= G.addNodo(tmp[i])
                origen.addAdyacente(destino)
                arco= Arco.Arco(1,origen,destino)
                G.addArco(arco)
G.BFS("r")
G.show()    
archivo.close()   
    
    
    
    
    
    
