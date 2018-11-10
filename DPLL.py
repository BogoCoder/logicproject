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

def DPLL(S, I):
	S, I = unitPropagate(S, I)
	print(S, I)
	if [] in S:
		return False, {}
	if len(S) == 0:
		return True, I
	else:
		return True, I

