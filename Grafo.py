
import Nodo
import math
import Arco
from time import time


class Grafo:
    base = dict()
    ord = dict()   

    def __init__(self):
        self.V = {}
        self.E = []

    def getV(self):
        return self.V

    def getE(self):
        return self.E

    def setE(self, E):
        self.E = E

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

    def sortByASC(self):
        lista = []
        for u in self.getV().values():
            lista.append(u)
        lista.sort(key=lambda x:x.f, reverse = False)
        v2 = {}
        for u in lista:
            v2[u.getNombre()] = u
            self.V = v2
        # print("tiempo: ", format(t2-t1))

    def find(self, g1, nombre):
        for n in g1.getV().values():
            # print("comparando: ",n.getNombre(), "con ", nombre)
            if n.getNombre() == nombre:
                return n
            # print("no encontro: ",nombre)
        return None

    def kruskal2(self):
        grafo = Grafo()
        na = 0
        for v in self.V.values():
            name = v.getNombre()
            print("name: ",name)
            n = Nodo.Nodo(name)
            na = na + 1
            n.setArbol(na);
            grafo.addNodo(n);
            v.setArbol(na)

        edges = list(self.E)
        edgesTmp = []
        menor = edges[0]
        # print("costo, o, d: ",arista.costo, arista.origen.getNombre(), arista.destino.getNombre())
        # print(len(edges))

        while(len(edges) > 0):
            for edge in edges:
                if edge.costo < menor.costo :
                    menor = edge;
                
            # print("menor ",menor.origen.getNombre(),"-",menor.destino.getNombre()," ",menor.costo
            #     ," a",menor.origen.getArbol(),":",menor.destino.getArbol())
            vx = menor.origen.getArbol()
            uy = menor.destino.getArbol()

            if vx != uy:
                na = na + 1
                for v2 in self.V.values():
                    if v2.getArbol() == vx or v2.getArbol() == uy:
                        v2.setArbol(na)

                on = grafo.find(self, menor.origen.getNombre())
                od = grafo.find(self, menor.destino.getNombre())
                arco = Arco.Arco(menor.costo, on, od)
                edgesTmp.append(arco)

            edges.remove(menor)
            if len(edges) > 0:
                menor = edges[0]

        for arco2 in edgesTmp:
            arco2.origen.addAdyacente(arco2.destino)
            arco2.destino.addAdyacente(arco2.origen)

        grafo.setE(edgesTmp)
        return grafo

    def make_set(self, v):
        self.base[v] = v
        self.ord[v] = 0

    # def find(self, v):
    #     if self.base[v] != v:
    #         self.base[v] = self.find(self.base[v])
    #     return self.base[v]

    def union(self, u, v):
        v1 = self.find(u)
        v2 = self.find(v)
        # print("u: ",u)
        # print("v: ",v)
        # print("v1: ",v1)
        # print("v2: ",v2)
        
        if v1 != v2:
            if self.ord[v1] > self.ord[v2]:
                self.base[v2] = v1 
            else:
                self.base[v1] = v2
                if self.ord[v1] == self.ord[v2]: 
                    self.ord[v2] += 1

    def kruskal(self):
        # A = {conjunto vacío}
        mst = set()
        for v in self.V.values():
            # print(v.getNombre())
            self.make_set(v.getNombre())
        # print ("Sub gráficos creados:")
        # print (self.base)

        # Ordena la lista G.E en forma no decendente por su peso w
        # En este caso usamos el ordenador dentro de python
        edges = list(self.E)
        edges.sort(key=lambda x:x.costo, reverse = False)
        
        # Para toda arista(u,v) en G.E
        for e in edges:
            weight = e.costo
            u = e.origen
            v = e.destino
            print(weight, u.getNombre(), v.getNombre())
            # Si encontrar-conjunto(u) != encontrar-conjunto(v)
            if self.find(u.getNombre()) != self.find(v.getNombre()):
                # A = A union (u,v)
                self.union(u.getNombre(), v.getNombre())
                # Union(u,v)
                mst.add(e)
        return mst
