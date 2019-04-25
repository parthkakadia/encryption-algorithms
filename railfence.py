def encrypt(pt, k, c):

    matrix = [[0 for x in range(c)] for y in range(k)]

    flag=0
    row=0
    col=0
    result=""

    for i in range(c):
        if row==0 or row==k-1:
            if flag==0:
                flag=1
            else:
                flag=0

        matrix[row][col]=pt[i]
        col=col+1

        if flag==1:
            row=row+1
        else:
            row=row-1

    for i in range(k):
        for j in range(c):
            if matrix[i][j]!=0:
                result+=matrix[i][j]

    print("Cipher text=" + result)

def decrypt(ct, k, c):
    matrix = [[0 for x in range(c)] for y in range(k)]

    flag = 0
    row = 0
    col = 0
    result2 = ""

    for i in range(c):
        if row == 0 or row == k - 1:
            if flag == 0:
                flag = 1
            else:
                flag = 0

        matrix[row][col] = "*"
        col = col + 1

        if flag == 1:
            row = row + 1
        else:
            row = row - 1

    ind=0
    for i in range(k):
        for j in range(c):
            if matrix[i][j]=='*' and ind<c:
                matrix[i][j]=ct[ind]
                ind=ind+1

    row=0
    col=0
    flag=0
    for i in range(c):
        if row==0 or row==k-1:
            if flag==0:
                flag=1
            else:
                flag=0
        if matrix[row][col]!=0:
            result2+=matrix[row][col]
            col=col+1

        if flag==1:
            row=row+1
        else:
            row=row-1

    print("Plain Text=" + result2)


key=input("Enter key")
plaintext=raw_input("Enter plain text")
column=len(plaintext)
encrypt(plaintext, key, column)

key1=input("Enter key")
ciphertext=raw_input("Enter cipher text")
column1=len(ciphertext)
decrypt(ciphertext, key1, column1)
