#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.d = 0
        self.f = 0
        self.p = None
        self.color = "Blanco"
        self.adjunta = []

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getD(self):
        return self.d

    def setD(self, d):
        self.d = d

    def getF(self):
        return self.f

    def setF(self, f):
        self.f = f

    def getP(self):
        return self.p

    def setP(self, p):
        self.p = p

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color
    
    def addAdyacente(self, nodo):
        self.adjunta.append(nodo)
    
    def getAdjunta(self):
        return self.adjunta
    
    def clearAdjunta(self):
        self.adjunta.clear
    
    def show(self):
        # print("(", end="")
        # print(self.nombre, self.d, self.f, self.color, sep=", ", end="")
        print(self.nombre, end="")
        print("(",self.d,"/", self.f,sep="", end="")

        print("):", end=" ")
        for adyacente in self.adjunta:
            print(adyacente.getNombre(), end=", ")
        print("")

    def show2(self):
        print("(", end="")
        print(self.nombre, self.d, self.f, self.color, self.p, sep=", ", end="")

        print("):", end=" ")
        for adyacente in self.adjunta:
            print(adyacente.getNombre(), end=", ")
        print("")
    
    def showN(self):
        print("", end="")
        print(self.nombre, sep=", ", end="")
        print("", end=" ")
        for adyacente in self.adjunta:
            print(adyacente.getNombre(), end=", ")
        print("")
    
    def showCSS(self, lista):
        i = 0
        for u in lista:
            print ("SCC: ",i+1)
            i = i + 1
            for v in u:
                print(v.getNombre(), end="")
                print("(",v.getD(),"/", v.getF(),sep="", end="")

                print("):", end=" ")
                for adyacente in v.getAdjunta():
                    print(adyacente.getNombre(), end=", ")
                print("")
            
        