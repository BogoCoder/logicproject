def unitPropagate(conjuntoClaus, interparcial):
	clausnocur = conjuntoClaus
	unit = False
	novoid = True
	ind = 0
	for i in range(len(conjuntoClaus)):
		if len(conjuntoClaus[i]) == 0:
			novoid = False
			break
		if len(conjuntoClaus[i]) == 1: 
			unit = True
			ind = i

	if(unit and novoid):
		current = conjuntoClaus[ind][0]
		if '-' in current:
			clausnocur = [x for x in conjuntoClaus if current not in x]
			for i in range(len(clausnocur)):
				clausnocur[i] = [x for x in clausnocur[i] if current[1:] != x]
		else:
			clausnocur = [x for x in conjuntoClaus if current not in x]
			for i in range(len(clausnocur)):
				clausnocur[i] = [x for x in clausnocur[i] if '-' + current != x]
		return unitPropagate(clausnocur, "nada")

	else:
		return clausnocur

	