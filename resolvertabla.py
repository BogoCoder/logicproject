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

## Regla 1: Solo hay un numero en cada casilla

R1 = '' # Para guardar la formula de la regla 1 en polaca inversa
inicial = True # Para inicializar la primera

for j in range(1, 3): #range(1, x) x-1 representa el numero de casillas. Para este caso trabajamos con las 2 primeras casillas por facilidad de ejecucion pero en realidad x=17.
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
    
    if j < 2: # j < x donde x representa el numero de casillas. Para este caso trabajamos con las 2 primeras casillas por facilidad de ejecucion pero en realidad x=16.
        R1 = 'OOO'+ R1 + 'Y'
   
#print "R1: ", R1


## Regla 2: Si hay un numero particular en una region, no debe haber otro numero igual en la misma region

reg1=['1','2','5','6']
reg2=['3','4','7','8']
reg3=['9','10','13','14']
reg4=['11','12','15','16']
regs=[reg1,reg2,reg3,reg4]

R2 = '' # Para guardar la formula de la regla 2 en polaca inversa
inicial = True # Para inicializar la primera conjuncion
#count = 0 contador temporal de subformulas de la regla
for i in range(1,3): #range(1, x) x-1 representa el numero de casillas. Para este caso trabajamos con las 2 primeras casillas por facilidad de ejecucion pero en realidad x=17.
    for k in range(4): 
        if str(i) in regs[k]: #verifica si i esta en una region particular
            for j in baslet: #itera sobre las letras proposicionales base
                literal = "YY"+j+str(i)+'Y' # forma base del final de la formula en polaca inversa
                for x in regs[k]: #itera sobre los numeros de las casillas de la region escogida
                    if x != str(i): #excluye el numero de la casilla donde va a estar el numero segun la regla
                        #print "x = " + x
                        #print "i = "+ str(i)
                        literal = j+x+'-'+literal # agrega las otras letras proposicionales segun la regla
                #literal corresponde a una subformula de la regla
                #print "/// " + literal # imprime subformulas
                #count+=1
                if inicial:
                    R2 = literal + 'OOO'
                    inicial = False
                else:
                    R2 = literal + R2
    
    if i < 2:# j < x donde x representa el numero de casillas. Para este caso trabajamos con las 2 primeras casillas por facilidad de ejecucion pero en realidad x=16.
        R2 = 'OOO'+ R2 + 'Y'
            #R2 es la formula general de las conjunciones de las subformulas 
            #print "*** "+R2 #imprime formula general
#print "total = "+str(count) # imprime numero total de subformulas

#print "R2: ", R2


## Regla 3: Si hay un numero particular en una fila, no debe haber otro numero igual en la misma fila

row1=['1','2','3','4']
row2=['5','6','7','8']
row3=['9','10','11','12']
row4=['13','14','15','16']
rows=[row1,row2,row3,row4]

R3 = '' # Para guardar la formula de la regla 3 en polaca inversa
inicial = True # Para inicializar la primera conjuncion
c = 0
#count = 0 contador temporal de subformulas de la regla
for i in range(1,3):#range(1, x) x-1 representa el numero de casillas. Para este caso trabajamos con las 2 primeras casillas por facilidad de ejecucion pero en realidad x=17.
    for k in range(4): 
        if str(i) in rows[k]: #verifica si i esta en una region particular
            for j in baslet: #itera sobre las letras porposicionales base
                literal = "YY"+j+str(i)+'Y' # forma base del final de la formula en polaca inversa
                for x in rows[k]: #itera sobre los numeros de las casillas de la region escogida
                    if x != str(i): #excluye el numero de la casilla donde va a estar el numero segun la regla
                        #print "x = " + x
                        #print "i = "+ str(i)
                        literal = j+x+'-'+literal # agrega las otras letras porposicionales segun la regla
                #literal corresponde a una subformula de la regla 
                #print "/// " + literal # imprime subformulas 
                #count+=1
                if inicial:
                    R3 = literal + 'OOO'
                    inicial = False
                else:
                    R3 = literal + R3
    
    if i < 2:# j < x donde x representa el numero de casillas. Para este caso trabajamos con las 2 primeras casillas por facilidad de ejecucion pero en realidad x=16.
        R3 = 'OOO'+ R3 + 'Y'
            #R3 es la formula general de las conjunciones de las subformulas
            #print "*** "+R3 #imprime formula general
#print "total = "+str(count) # imprime numero total de subformulas

#print "R3: ", R3

## Regla 4: Si hay un numero particular en una columna, no debe haber otro numero igual en la misma columna

column1=['1','5','9','13']
column2=['2','6','10','14']
column3=['3','7','11','15']
column4=['4','8','12','16']
columns=[column1,column2,column3,column4]

R4 = '' # Para ir guardando las disyunciones de cuartetos de disyunciones de literales
inicial = True # Para inicializar la primera conjuncion
#count = 0 contador temporal de subformulas de la regla
for i in range(1,3): #range(1, x) x-1 representa el numero de casillas. Para este caso trabajamos con las 2 primeras casillas por facilidad de ejecucion pero en realidad x=17.
    for k in range(4): 
        if str(i) in columns[k]: #verifica si i esta en una region particular
            for j in baslet: #itera sobre las letras porposicionales base
                literal = "YY"+j+str(i)+'Y' # forma base del final de la formula en polaca inversa
                for x in columns[k]: #itera sobre los numeros de las casillas de la region escogida
                    if x != str(i): #excluye el numero de la casilla donde va a estar el numero segun la regla
                        #print "x = " + x
                        #print "i = "+ str(i)
                        literal = j+x+'-'+literal # agrega las otras letras porposicionales segun la regla
                #literal corresponde a una subformula de la regla 
                #print "/// " + literal # imprime subformulas 
                #count+=1
                if inicial:
                    R4 = literal + 'OOO'
                    inicial = False
                else:
                    R4 = literal + R4
    
    if i < 2:# j < x donde x representa el numero de casillas. Para este caso trabajamos con las 2 primeras casillas por facilidad de ejecucion pero en realidad x=16.
        R4 = 'OOO'+ R4 + 'Y'
            #R4 es la formula general de las conjunciones de las subformulas
            #print "*** "+R4 #imprime formula general
#print "total = "+str(count) # imprime numero total de subformulas

#print "R4: ", R4


sudoq = "p1r6s7q10p14r16YYYYY" # sudoku a resolver, ejemplo

# Creo las formulas como objeto
A = T.StringtoTree(R1, letrasProposicionales) #para regla 1
print "\nFormula 1: ", T.Inorder(A)
B = T.StringtoTree(R2, letrasProposicionales) #para regla 2
print "\nFormula 2: ", T.Inorder(B)
C = T.StringtoTree(R3, letrasProposicionales) #para regla 3
print "\nFormula 3: ", T.Inorder(C)
D = T.StringtoTree(R4, letrasProposicionales) #para regla 4
print "\nFormula 4: ", T.Inorder(D)
Z = T.StringtoTree(sudoq, letrasProposicionales) # para ejemplo
print "\nFormula parcial: ", T.Inorder(Z)

lista_hojas = [[A,B,C,D,Z]] # Inicializa la lista de hojas

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
            print contador, ": ", "Trabajando con literales: ", i
            V.dibujar_tablero(i,contador)
            contador += 1

print "FIN"
