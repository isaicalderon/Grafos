#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 09:16:57 2019

@author: lbeltran
"""
import Nodo
import math

class Grafo:
    def __init__(self):
        self.V={}
        self.E=[]
    def getV(self):
        return self.V
    def getE(self):
        return self.E
    def addNodo(self,nombre):
        if nombre not in self.V:
            nodo= Nodo.Nodo(nombre)
            self.V[nombre]=nodo
        return self.V[nombre]
    def addArco(self,arco):
        self.E.append(arco)
        
    def show(self):
        for nodo in self.V.values():
            nodo.show()
            
    def BFS(self,nombre):
        Q=[]
        for u in self.V.values():
            u.setColor("Blanco")
            u.setD(math.inf)
            u.setP(None)
        u=self.V[nombre]
        u.setD(0)
        u.setColor("Gris")
        Q.append(u)
        while len(Q)>0:
            u=Q[0]
            for v in u.getAdjunta():
                if(v.getColor()=="Blanco"):
                    v.setColor("Gris")
                    v.setD(u.getD()+1)
                    v.setP(u)
                    Q.append(v)
            del(Q[0])
            u.setColor("Negro")
    
    
    
    
    
    
    
    
    
    