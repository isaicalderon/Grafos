
import Nodo
import math
import Arco
from time import time


class Grafo:
    def __init__(self):
        self.V = {}
        self.E = []

    def getV(self):
        return self.V

    def getE(self):
        return self.E

    def addNodo(self, nombre):
        if nombre not in self.V:
            nodo = Nodo.Nodo(nombre)
            self.V[nombre] = nodo
        return self.V[nombre]

    def getNodo(self, nombre):
        if nombre in self.V.keys():
            return self.V[nombre]
            
    def addArco(self, arco):
        self.E.append(arco)
        
    def show(self):
        for nodo in self.V.values():
            nodo.show()

    def show2(self):
        for nodo in self.V.values():
            nodo.show2()
    
    def showNodos(self):
        for nodo in self.V.values():
            nodo.showN()

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
            print("\n")
    
    def showOrdenTopo(self):
        for nodo in self.V.values():
            print(nodo.getNombre(), sep="",end=", ")
        print("")

    def BFS(self, nombre):
        Q = []
        for u in self.V.values():
            u.setColor("Blanco")
            u.setD(math.inf)
            u.setP(None)
        u = self.V[nombre]
        u.setD(0)
        u.setColor("Gris")
        Q.append(u)
        while len(Q) > 0:
            u = Q[0]
            for v in u.getAdjunta():
                if v.getColor() == "Blanco":
                    v.setColor("Gris")
                    v.setD(u.getD()+1)
                    v.setP(u)
                    Q.append(v)
            del(Q[0])
            u.setColor("Negro")
    
    def DFS(self):
        tiempo = 0
        for u in self.V.values():
            u.setColor("Blanco")
            u.setD(math.inf)
            u.setF(math.inf)
            u.setP(None)
        # end for
        for u in self.V.values():
            if u.getColor() == "Blanco":
                tiempo = self.DFSVisit(u, tiempo)
            # end if
        # end for

    def DFSVisit(self, u, tiempo):
        u.setColor("Gris")
        tiempo = tiempo + 1;
        u.setD(tiempo)
        for v in u.getAdjunta():
            if v.getColor() == "Blanco":
                # Aqui esta la clave del exito, hechale mas ganas prro
                # print("Ya se descubrio el nodo ",u.getNombre())
                
                tiempo = self.DFSVisit(v, tiempo)
            # end if
        # end for
        u.setColor("Negro")
        tiempo+=1
        u.setF(tiempo)
        return tiempo 

    def getTrans(self):
        gt = Grafo()
        for u in self.getV().values():
            gt.addNodo(u.getNombre())
        # end for
        for a in self.getE():
            origen = gt.getNodo(a.destino.getNombre())
            destino = gt.getNodo(a.origen.getNombre())
            arco = Arco.Arco(a.costo, origen, destino)
            gt.addArco(arco)
            origen.addAdyacente(destino)
        # end for
        return gt

    def SCC(self):
        lista = []
        tiempo = 0
        for u in self.V.values():
            u.setColor("Blanco")
            u.setD(math.inf)
            u.setF(math.inf)
            u.setP(None)
        # end for
        for u in self.V.values():
            if u.getColor() == "Blanco":
                lista2 = []
                lista.append(lista2)
                tiempo = self.SCCVisit(u, tiempo, lista2)
            # end if
        # end for
        return lista;
    # FIN SCC

    def SCCVisit(self, u, tiempo, lista):
        lista.append(u)
        u.setColor("Gris")
        tiempo = tiempo + 1;
        u.setD(tiempo)
        for v in u.getAdjunta():
            if v.getColor() == "Blanco":
                tiempo = self.SCCVisit(v, tiempo, lista)
        u.setColor("Negro")
        tiempo+=1
        u.setF(tiempo)
        return tiempo 
    # FIN SCCVisit

    def sortByFDesc(self):
        lista = []
        t1 = time()
        for u in self.getV().values():
            lista.append(u)
        lista.sort(key=lambda x:x.f, reverse = True)
        v2 = {}
        for u in lista:
            v2[u.getNombre()] = u
            self.V = v2
        t2 = time()
        # print("tiempo: ", format(t2-t1))

    def MST_KRUSKAL(self, G):
        a = 0
        for v in self.getV().values():          
            make_set(v)
        