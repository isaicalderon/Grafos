#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 09:16:35 2019

@author: lbeltran
"""

class Nodo:
    def __init__(self, nombre):
        self.nombre=nombre
        self.d=0
        self.f=0
        self.p=None
        self.color="Blanco"
        self.adjunta=[]
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre=nombre
    def getD(self):
        return self.d
    def setD(self, d):
        self.d=d
    def getF(self):
        return self.f
    def setF(self, f):
        self.f=f
    def getP(self):
        return self.p
    def setP(self, p):
        self.p=p
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color=color
    def addAdyacente(self,nodo):
        self.adjunta.append(nodo)
    def getAdjunta(self):
        return self.adjunta
    def clearAdjunta(self):
        self.adjunta.clear
    def show(self):
        print("(",end="")
        print(self.nombre,self.d,self.f,self.color,sep=", ",end="")
        print("):",end=" ")
        for adyacente in self.adjunta:
            print(adyacente.getNombre(),end=", ")
        print("")