import re
import math
import Nodo 
import Arco
import Grafo
g = Grafo.Grafo()
    
def realizar_datos(archivo):

    archivo = open("entradas/"+archivo)
    costo   = "X"
    g       = Grafo.Grafo()

    linea   = archivo.readline()
    linea   = linea.rstrip()
    linea   = linea.strip()
    tmpD    = re.findall("^dirigido\s*=\s*(\S+)",linea)
    linea   = archivo.readline()
    linea   = linea.rstrip()
    linea   = linea.strip()
    tmp     = re.findall("^costo\s*=\s*(\S+)",linea)
        

    if len(tmp) > 0:
        costo = tmp[0]
    # end if
    if len(tmpD) > 0:
        dirigido = tmpD[0]

    if(costo == "no"):
        for linea in archivo.readlines():
            linea = linea.rstrip()
            linea = linea.strip()
            tmp = re.findall("\S+",linea)
            if len(tmp) > 0:
                origen = g.addNodo(tmp[0])

                for i in range(1, len(tmp)):
                    destino = g.addNodo(tmp[i])
                    origen.addAdyacente(destino)
                    if dirigido == "no":
                        origen.addAdyacente(destino)
                    arco = Arco.Arco(1, origen, destino)
                    g.addArco(arco)
                # end for
            # end if
        # end for
    elif costo == "si":
        for linea in archivo.readlines():
            linea = linea.rstrip()
            linea = linea.strip()
            tmp = re.findall("\S+", linea)
            # print (costo)
        # end for
            if len(tmp) > 0:
                origen = g.addNodo(tmp[0])
                for i in range(1, len(tmp)):
                    name = re.findall("(\S+)\s*:", tmp[i]);
                    costo = re.findall(":\s*(\S+)", tmp[i])
                    name = name[0]
                    costo = float(costo[0])
                    destino = g.addNodo(name)
                    origen.addAdyacente(destino)
                    if dirigido == "no":
                        origen.addAdyacente(destino)
                    arco = Arco.Arco(costo, origen, destino)
                    g.addArco(arco)
                # end for
            # end if
        # end for
    # end elif
    archivo.close()

entrada1 = "entrada1.txt";
entrada2 = "entrada2.txt";

# menu
print("Seleccione una opcion: ")
print("[1]. BFS - Entrada 1")
print("[2]. BFS - Entrada 2")
print("[3]. DFS - Entrada 1")
print("[4]. DFS - Entrada 2")
print("[5]. Transpuesto - Entrada 1")
print("[6]. Transpuesto - Entrada 2")
print("[7]. SCC - Entrada 1")
print("[8]. Ordenamiento Topologico - Entrada 1")
print("[9]. Ordenamiento Topologico - Entrada 2")
print("[10]. Krauskal - Entrada 1")

num = int(input(" => "))
if num == 1:
    archivo = "BFS"+"/"+entrada1;
    nodo = input("Iniciar con el Nodo: ")
    print(nodo)
    realizar_datos(archivo)
    g.BFS('s')
    g.show()
if num == 2:
    archivo = "BFS"+"/"+entrada2;





# print("G:")
# g.BFS('s')
# g.sortByFDesc()

# g.DFS()
# g.show()
# g.sortByFDesc()
# print("\nOrden topologico: ")
# g.showOrdenTopo()
# print("\nGT: ")
# gt = g.getTrans()
# lista = gt.SCC()
# gt.showCSS(lista)
