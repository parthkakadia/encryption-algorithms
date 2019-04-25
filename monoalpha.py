def encrypt(K,P):
	r="abcdefghijklmnopqrstuvwxyz"
	c=""
	for i in P:
		c=c+r[K.find(i)]
	return c

def decrypt(K,C):
	r="abcdefghijklmnopqrstuvwxyz"
	p=""
	for i in C:
		p=p+K[r.find(i)]
	return p



print "1. Encryption\n2. Decryption"
c=input("You want to..?? ")
K="zyxwvutsrqponmlkjihgfedcba"
if c==1:
	print "Encryption"
	P = raw_input("Plain Text: ")
	#K = input('Key: ')
	print "\n\nKey:\t\t", K , "\nPlain Text:\t",P
	C=encrypt(K,P)
	print "Cipher Text:\t",C
elif c==2:
	print "Decryption"
	C = raw_input("Cipher Text: ")
	#K = input('Key: ')
	print "\n\nKey:\t\t", K , "\nPlain Text:\t",C
	P=decrypt(K,C)
	print "Cipher Text:\t",P