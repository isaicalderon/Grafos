import leerArchivoEntrada

entrada1 = "entrada1.txt";
entrada2 = "entrada2.txt";
leer = leerArchivoEntrada()

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
if num == 2:
    archivo = "BFS"+"/"+entrada2;

print(archivo)

leer.fun(archivo)