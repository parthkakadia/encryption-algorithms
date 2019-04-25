def encrypt(Key,PT):
    P=list(PT)
    K=int(Key)
    s=len(P)
    c=int((s-1)/(K-1))
    if c%2==0 :
        num=[]
        last=c-1
        num.append(c)
        extra=(s-1)%(K-1)
        for i in range(1,K-1):
            if extra>0:
                num.append(c+1)
                extra-=1
            else :
                num.append(c)
        num.append(last)
        keysToAns = []
        for i in range(K):
            keysToAns.append(-1)
        ans=[]
        for i in range(int(s/(K-1))+1):
            f=(i%(K-1))%2
            print("------------------------")
            if f==0:
                start=2*(K-1)*int(i/2)
                end=2*(K-1)*int(i/2)+(K-1)
                if end>s:
                    end=s
                for x in range(start,end):
                    print(x)
                    ans.insert(keysToAns[int(x%(K-1))]+1,P[x])
                    for y in range(x%(K-1),len(keysToAns)):   
                        keysToAns[y]  += 1
                    print(keysToAns)
                    print(ans)
                    print("****")
            
            else :
                start=2*(K-1)*int((i-1)/2)+(K-1)
                end=2*(K-1)*(int(i/2)+1)
                if end>s:
                    end=s
                for x in range(start,end):
                    print(x)
                    ans.insert(keysToAns[K-(x%(K-1))-1]+1,P[x])
                    for y in range(K-(x%(K-1))-1,len(keysToAns)):   
                        keysToAns[y]  += 1
                    print(keysToAns)
                    print(ans)
                    print("****")
    print("-------------------------------------------------------------------------------------")
    print(ans)
    print("-------------------------------------------------------------------------------------")

K = input("Key: ")
P = input("Plain Text: ")
encrypt(K,P)
