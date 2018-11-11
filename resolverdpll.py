print("Importando paquetes...")
from timeit import default_timer as timer
import cnf as cnf
import DPLL as dpll
print(u"¡Importados!")

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

###### Importante: variable 'val' ######
val = 16 # val representa el numero de casillas.
# Para este caso base trabajamos con las 2 primeras casillas por facilidad de ejecucion (val=2)
# pero en realidad val debe ser 16, el sudoku completo.

## Regla 1: Solo hay un numero en cada casilla

R1 = '' # Para guardar la formula de la regla 1 en polaca inversa
inicial = True # Para inicializar la primera

for j in range(1, val+1):
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
            R1 = literal + 'OOO'
            inicial = False
        else:
            R1 = literal + R1
    
    if j < val:
        R1 = 'OOO'+ R1 + 'Y'
   
#print ("R1: ", R1)

conjuntoClaus = [['p','q','r'], ['-p','-q','-r'], ['-p','q','r'], ['-q','r'], ['q','-r']]
#conjuntoClaus = cnf.toclaus(R1, letrasProposicionales)
interps = {}
OK, interps = dpll.DPLL(conjuntoClaus, interps)
if OK:
	print("Satisfacible!")
	print(OK, interps)
else:
	print("Nada!")
	print(OK, interps)
