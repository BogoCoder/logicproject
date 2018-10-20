#-*-coding: utf-8-*-

# Basado en el codigo de Edgar Andrade, Octubre 2018
# Camilo Martinez y Samuel Perez
# Codigo para crear la formula para la resolucion de sudokus

print "Importando paquetes..."
from timeit import default_timer as timer
import Tableaux as T
print "Importados!"

# Guardo el tiempo al comenzar el procedimiento
start = timer()

#Letras proposicionales basicas
baslet = ['p', 'q', 'r', 's'] 

# Creo las letras proposicionales
letrasProposicionales = []
for i in range(1, 17):
    for o in baslet:
            letrasProposicionales.append(o + str(i))

# print "Letras proposicionales: ", letrasProposicionales

# Regla 1: Solo hay un numero en cada casilla
disyunciones = '' # Para ir guardando las disyunciones de cuartetos de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion

for j in range(1,17):
    aux1 = [x for x in letrasProposicionales if x[1:] == str(j)]
    #print "aux1: " , aux1
    for u in aux1:
        aux2 = [x for x in aux1 if x != u]
        literal = u
        #print "aux2 " , aux2
        for v in aux2:
                literal = v + '-' + literal + "Y"
        #print "literal : " + literal
        if inicial: 
            disyunciones = literal
            inicial = False
        else:
            disyunciones = literal + disyunciones + 'O'

        # print "Disyunciones: ", disyunciones

## Comento esto para que se pueda ver el funcionamiento con la primera regla
# Esta parte no la he modificado
"""

# Regla 2: Ningun caballo debe poder atacar a otro

disyunciones = '8-6-Y1>' + disyunciones + 'Y'
disyunciones = '9-7-Y2>' + disyunciones + 'Y'
disyunciones = '8-4-Y3>' + disyunciones + 'Y'
disyunciones = '9-3-Y4>' + disyunciones + 'Y'
disyunciones = '7-1-Y6>' + disyunciones + 'Y'
disyunciones = '6-2-Y7>' + disyunciones + 'Y'
disyunciones = '3-1-Y8>' + disyunciones + 'Y'
disyunciones = '4-2-Y9>' + disyunciones + 'Y'

"""

# Creo la formula como objeto

A = T.StringtoTree(disyunciones, letrasProposicionales)
print "Formula: ", T.Inorder(A)

lista_hojas = [[A]] # Inicializa la lista de hojas

OK = '' # El tableau regresa Satisfacible o Insatisfacible
interpretaciones = [] # lista de lista de literales que hacen verdadera lista_hojas

OK, INTS = T.Tableaux(lista_hojas, letrasProposicionales)

print "Tableau terminado!"
# Guardo el tiempo al terminar el procedimiento
end = timer()
print u"El procedimiento demoró: ", end - start

if OK == 'Satisfacible':
    if len(INTS) == 0:
        print u"Error: la lista de interpretaciones está vacía"
    else:
        print "Guardando interpretaciones en archivo..."
        import csv
        archivo = 'tableros_automatico.csv'
        with open(archivo, 'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(INTS)

        print "Interpretaciones guardadas  en " + archivo

        import visualizacion as V
        contador = 1
        for i in INTS:
            print "Trabajando con literales: ", i
            V.dibujar_tablero(i,contador)
            contador += 1

print "FIN"
