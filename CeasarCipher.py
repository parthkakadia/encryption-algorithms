def encrypt(K, P):
    pa = list(P)
    for i in pa:
        pa[pa.index(i)] = chr(ord(i) + K)
    pa.reverse()
    C = ''.join(str(i) for i in pa)
    return C


def decrypt(K, C):
    ca = list(C)
    for i in ca:
        ca[ca.index(i)] = chr(ord(i) - K)
    ca.reverse()
    P = ''.join(str(i) for i in ca)
    return P


print("1. Encryption\n2. Decryption")
c = int(input("You want to..?? "))
if c == 1:
    print("Encryption")
    P = input("Plain Text: ")
    K = int(input('Key: '))
    print("\n\nKey:\t\t", K, "\nPlain Text:\t", P)
    C = encrypt(K, P)
    print("Cipher Text:\t", C)
elif c == 2:
    print("Decryption")
    C = input("Cipher Text: ")
    K = int(input('Key: '))
    print("\n\nKey:\t\t", K, "\nPlain Text:\t", C)
    P = decrypt(K, C)
    print("Cipher Text:\t", P)
