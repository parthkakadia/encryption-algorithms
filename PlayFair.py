def mat(K):
	matrix=[]
	for e in K.upper():
		if e not in matrix:
			matrix.append(e)
	alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ"	
	for e in alpha:
		if e not in matrix:
			matrix.append(e)
	KM=[]
	for i in range(0,5):
		KM[i]=KM.append('')
	for i in range(0,5):
		KM[i]=matrix[i*5:(i+1)*5]
	return KM
def encrypt(K,P):
	KM=mat(K)
	PL=list(P.upper())
	for i in range(0,len(PL)-1,2):
		if(PL[i]==PL[i+1]):
			PL.insert(i+1,'X')
	if(len(PL)%2==1):
		PL.append("X")		
	r1=r2=c1=c2=0
	C=[]
	for i in range(0,len(PL)-1,2):
		for j in range(0,5):
			for k in range(0,5):
				if(PL[i]==KM[j][k]):
					r1=j
					c1=k
				if(PL[i+1]==KM[j][k]):
					r2=j
					c2=k
		if(c1==c2):
			if(r1==4):
				r1=-1
			if(r2==4):
				r2=-1
			C.append(KM[r1+1][c1])
			C.append(KM[r2+1][c2])
		elif(r1==r2):
			if(c1==4):
				c1=-1
			if(c2==4):
				c2=-1
			C.append(KM[r1][c1+1])
			C.append(KM[r2][c2+1])
		else:
			C.append(KM[r1][c2])
			C.append(KM[r2][c1])
	CT=''.join(C)
	return CT
def decrypt(K,C):
	KM=mat(K)
	CL=list(C.upper())
	r1=r2=c1=c2=0
	P=[]
	for i in range(0,len(CL)-1,2):
		for j in range(0,5):
			for k in range(0,5):
				if(CL[i]==KM[j][k]):
					r1=j
					c1=k
				if(CL[i+1]==KM[j][k]):
					r2=j
					c2=k
		if(c1==c2):
			if(r1==0):
				r1=5
			if(r2==0):
				r2=5
			P.append(KM[r1-1][c1])
			P.append(KM[r2-1][c2])
		elif(r1==r2):
			if(c1==0):
				c1=5
			if(c2==0):
				c2=5
			P.append(KM[r1][c1-1])
			P.append(KM[r2][c2-1])
		else:
			P.append(KM[r1][c2])
			P.append(KM[r2][c1])
	PT=''.join(P)
	return PT


K = raw_input("Key: ")
P = raw_input("Plain Text: ")
CT=encrypt(K,P)
PT=decrypt(K,CT)
print "Cipher Text: "+CT
print "Plain Text: "+PT