def unitPropagate(S, I):
	Sx = S
	print(u"Realizando Unit Propagation a:", Sx)
	unit = False
	novoid = True
	ind = 0
	for i in range(len(S)):
		if len(S[i]) == 0:
			novoid = False
			break
		if len(S[i]) == 1: 
			unit = True
			ind = i

	if(unit and novoid):
		current = S[ind][0]
		if '-' in current:
			dictmp={current[1:]:False}
			I.update(dictmp)
			Sx = [x for x in S if current not in x]
			for i in range(len(Sx)):
				Sx[i] = [x for x in Sx[i] if current[1:] != x]
		else:
			dictmp={current:True}
			I.update(dictmp)
			Sx = [x for x in S if current not in x]
			for i in range(len(Sx)):
				Sx[i] = [x for x in Sx[i] if '-' + current != x]
		return unitPropagate(Sx, I)

	else:
		print(u"Fin de Unit Propagate:", Sx)
		return Sx, I

def assign(S, I, lit):
	Sx = S
	Ix = I
	x = lit[0]
	if '-' in x:
		dictmp={x[1:]:False}
		Ix.update(dictmp)
		Sxx = [Cl for Cl in Sx if x not in Cl]
		for Ci in range(len(Sxx)):
			Sxx[Ci] = [l for l in Sxx[Ci] if x[1:] != l]
	else:
		dictmp={x:True}
		Ix.update(dictmp)
		Sxx = [Cl for Cl in Sx if x not in Cl]
		for Ci in range(len(Sxx)):
			Sxx[Ci] = [l for l in Sxx[Ci] if '-' + x != l]			

	return Sxx, Ix

def DPLL(S, I):
	Sx, Ix = unitPropagate(S, I)
	if [] in Sx:
		return False, {}
	elif len(Sx) == 0:
		return True, Ix
	else:
		for C in Sx:
			lit = [x for x in C if x not in Ix]
		Sxx, Ixx = assign(Sx, Ix, lit)
		print(Sxx, Ixx)
		OK, Ir = DPLL(Sxx, Ixx)
		if OK == True:
			return True, Ir
		else:
			return False, {}

