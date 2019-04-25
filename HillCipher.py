import numpy as np
from numpy.linalg import inv
from numpy.linalg import det
 
def encrypt(K,P):
	#PM=build_matrix_PT(P)
	KM=build_matrix_key(K)
	P=P.upper()
	P=list(P)
	CT=[]
	if len(P)%2!=0:
		P.append('X')
	for i in range(0,len(P),2):
		PT=[]
		C=[]
		PT.append(ord(P[i])-65)
		PT.append(ord(P[i+1])-65)
		C=np.dot(KM,PT)
		CT.append(chr((C[0]%26)+65))
		CT.append(chr((C[1]%26)+65))
	CT=''.join(CT)
	return CT

def dinv(num):
	abc=0
	for i in range(1000):
		a=int(i*num)
		if a%26==1:
			abc=i
			break
	return abc

def decrypt(K,C):
	C=C.upper()
	C=list(C)
	KM=build_matrix_key(K)
	KM=np.array(KM)
	KMadj=inv(KM)*det(KM)
	KMadj=KMadj.astype(int)
	din=dinv(det(KM))
	Kin=(KMadj*din)%26
	PT=[]
	for i in range(0,len(C),2):
		PCT=[]
		P=[]
		PCT.append(ord(C[i])-65)
		PCT.append(ord(C[i+1])-65)
		P=np.dot(Kin,PCT)
		PT.append(chr((int(P[0])%26)+65))
		PT.append(chr((int(P[1])%26)+65))
	PT=''.join(PT)
	return PT

def build_matrix_key(K):
	K=K.upper()
	KM=[]
	for i in range(2):
		KM[i]=KM.append('')
	KM[0]=[ord(K[0])-65,ord(K[1])-65]
	KM[1]=[ord(K[2])-65,ord(K[3])-65]
	return KM



K = raw_input("Key: ")
P = raw_input("Plain Text: ")
CT=encrypt(K,P)
print "Encrypt: "+CT
PT=decrypt(K,CT)
print "Decrypt: "+PT