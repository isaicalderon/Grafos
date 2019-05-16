
import Nodo
import math
import Arco
from time import time


class Grafo:
    def __init__(self):
        self.V = {}
        self.E = []
        self.MAX_VALUE = 2147483647

    def getV(self):
        return self.V

    def getV2(self, num):
        return self.V.get(num)

    def getE(self):
        return self.E

    def setE(self, E):
        self.E = E

    def addNodo(self, nombre):
        if nombre not in self.V:
            nodo = Nodo.Nodo(nombre)
            self.V[nombre] = nodo
        return self.V[nombre]

    def addNodo2(self, nodo):
        if nodo.getNombre() not in self.V:
            # nodo = Nodo.Nodo(nombre)
            self.V[nodo.getNombre()] = nodo
            # print("se agrego el nodo: ",nodo.getNombre())
        return nodo.getNombre()

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
            print("nombre", nodo.nombre)
    
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

    def find(self, nombre):
        for n in self.V.values():
            # print("comparando: ", n.getNombre(), "con ", nombre)
            if n.getNombre() == nombre:
                return n
            # print("no encontro: ", nombre)
        return None

    def kruskal2(self):
        grafoTmp = Grafo()
        na = 0
        for v in self.V.values():
            name = v.getNombre()
            n = Nodo.Nodo(name)
            na = na + 1
            n.setArbol(na);
            grafoTmp.addNodo2(n) 
            # print("grafo creado: ", grafoTmp.getNodo(n.getNombre()))
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

                on = grafoTmp.find(menor.origen.getNombre())
                od = grafoTmp.find(menor.destino.getNombre())
                arco = Arco.Arco(menor.costo, on, od)
                # print("edge: ",on.getNombre(),", ",od.getNombre(),", ",menor.costo)
                edgesTmp.append(arco)
                # grafoTmp.addArco(arco)
            edges.remove(menor)
            if len(edges) > 0:
                menor = edges[0]
                # print("nuevo menor: ",menor.origen.getNombre())
        # end while

        for arco2 in edgesTmp:
            arco2.origen.addAdyacente(arco2.destino)
            arco2.destino.addAdyacente(arco2.origen)
            # grafoTmp.addArco(arco2)
            # print("arco2 origen:", arco2.origen.getNombre())
            # print("arco2 destino:", arco2.destino.getNombre()   )
                
        grafoTmp.setE(edgesTmp)
        return grafoTmp

    def prim(self):
        gPrim = Grafo()
        edges = list(self.E)
        lst = list(self.V.items())
        gPrim.addNodo(lst[0][1].getNombre())
        m = self.MAX_VALUE
        arcoAux = Arco.Arco(1, Nodo.Nodo(""), Nodo.Nodo(""))
        boolNa = False

        while True:
            for arco in edges:
                for nodo in gPrim.getV().values():
                    
                    c1 = gPrim.find(arco.origen.getNombre()) != None
                    c2 = gPrim.find(arco.destino.getNombre()) != None
                    
                    if (c1 and (not c2)) or (c2 and (not c1)) : 
                        # print("arco-Or: ",arco.origen.getNombre()," equalsTo ",nodo.getNombre())
                        if arco.origen.getNombre() == nodo.getNombre() and arco.costo <= m:
                            m = arco.costo
                            arcoAux = arco
                            boolNa = False
                        
                        if arco.destino.getNombre() == nodo.getNombre() and arco.costo <= m:
                            m = arco.costo
                            arcoAux = arco
                            boolNa = True
                # end for
            # end for
            print(boolNa)
            if boolNa == True:
                gPrim.addNodo(arcoAux.origen.getNombre())
            else:
                gPrim.addNodo(arcoAux.destino.getNombre())
            
            # print("remove", arcoAux.origen.getNombre())
            edges.remove(arcoAux)

            arcoAux =  Arco.Arco(m, gPrim.find(arcoAux.origen.getNombre()), gPrim.find(arcoAux.destino.getNombre()))

            gPrim.addArco(arcoAux)

            m = 2147483647

            # print("gPrim.V size: ",len(gPrim.getV())," contra V size: ",len(self.V))
            if len(gPrim.getV()) >= len(self.V):
                break
       # end while

        for arco2 in gPrim.getE():
            arco2.origen.addAdyacente(arco2.destino)
            arco2.destino.addAdyacente(arco2.origen)

        return gPrim
                                      
    def Boruvka(self):
        gBoruvka = Grafo()
        cola = list()

        edges = list(self.E)
        edgesTmp = list()

        for nodo in self.V.values():
            gtmp = Grafo()
            n = Nodo.Nodo(nodo.getNombre())
            gtmp.addNodo2(nodo)
            cola.append(gtmp)
            gBoruvka.addNodo2(n)
        # end for

        while len(cola) > 1:
            gt = cola.pop(0)
            arcoAux = None
            mv = self.MAX_VALUE
            bl = False

            for nodo in gt.getV().values():
                for arco in edges:
                    if (arco.origen.getNombre() == nodo.getNombre() or arco.destino.getNombre() == nodo.getNombre()):
                        if (arco.costo <= mv):
                            mv = arco.costo
                            print("agregando arco: ",arco.destino.getNombre())
                            arcoAux = arco;
                            if (arco.origen.getNombre() == nodo.getNombre()):
                                bl = True;
                            else:
                                bl = False;
            # end for
            print("remove: ",arcoAux.origen.getNombre())
            edges.remove(arcoAux)
            bl2 = False

            for arco in gBoruvka.getE():
                cb1 = arco.origen.getNombre()  == arcoAux.origen.getNombre()
                cb2 = arco.destino.getNombre() == arcoAux.destino.getNombre()
                print(cb1, cb2)
                if cb1 and cb2:
                    bl2 = True
            # end for
            
            if not bl2:
                arcotmp = Arco.Arco(arcoAux.costo, gBoruvka.find(arcoAux.origen.getNombre()), gBoruvka.find(arcoAux.destino.getNombre()))
                gBoruvka.addArco(arcotmp)

                bEncontrado = False
                c1 = 0

                while True:
                    c2 = 0
                    e2 = False
                    while True:
                        f = ""
                        
                        if bl == True:
                            f = arcoAux.destino.getNombre()
                        else:
                            f = arcoAux.origen.getNombre()

                        lst = list(cola[c1].getV().items())
                        
                        print(c2)

                        print("cola: ", lst[c2][1].getNombre()," - f: ", f)

                        if lst[0][1].getNombre() == f:
                            e2 = True
                            encontrado = True

                            # for (Nodo nx : cola.get(c1).getV()) :
                            for nodo in cola[c1].getV().values():
                                gt.addNodo2(nodo);
                            
                            # cola.remove(c1);
                            del cola[c1]
                            cola.append(gt)

                        if (e2 == False):
                            c2 += 1

                        if not (c2 < len(cola[c1].getV()) and (not e2)):
                            break
                    # end while 
                    if (not encontrado):
                        c1+=1
                    
                    if not (c1 < len(cola) and not encontrado):
                        break;
                # end while

        # end while
        for arco2 in gBoruvka.getE():
            arco2.origen.addAdyacente(arco2.destino)
            arco2.destino.addAdyacente(arco2.origen)

        return gBoruvka


