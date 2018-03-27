def feladat_3(n):
    tomb=[]
    for i in range(n):
        x=int(input())
        tomb.append(x)


    return sum(tomb)/n


def feladat_1(n):
    tomb=[]
    for i in range(n):
        x=int(input())
        tomb.append(x)


    return tomb


def feladat_2(n):
    szparatlan=0
    szparos=0
    while n>=1 and n<=100:
        s=int(input())
        if s%2==0:
            szparos+=s
        else:
            szparatlan+=s

    return szparos/szparatlan

def feladat_5(n):
    tomb=[]
    for i in range(n):
        x = int(input())
        tomb.append(x)
        if tomb[i]<7:
            a=tomb[i]**2
        if tomb[i]>10:
            b=sum(tomb[i])
    return a
    return b



def rel_prim(t,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if lnko(t[i],t[j])!=1:
                return False
    return True










def feladat_9(tomb,n):

    for i in range(n):
        k=rel_prim(tomb[i],n)
        if k==True:
            return 1
        else:
            return 0
        







import numpy as np
def hatos(n,m):
    #hat=np.array((n,m),dtype='int')
    hat=np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            if i==0 or i==n-1 or i==n//2:
                hat[i][j]=42
            else:
                hat[i][j]=32
        hat[i][0]=42
        if i>n//2:
            hat[i][m-1]=42

    for i in range(n):
        for j in range(m):
            print(chr(int(hat[i][j])),end=' ')
        print('\n')
def main():
    esetek = int(input())
    t=np.zeros(2*esetek,dtype='int')
    for i in range(0,2*esetek,2):
       sor=input()
       sor=sor.strip()
       sor=sor.split()
       t[i]=int(sor[0])
       t[i+1]=int(sor[1])
    #print(t)
    for i in range(0,2*esetek,2):
       hatos(t[i],t[i+1])
main()






def feladat_14():
    leg=0
    for i in range(0,n):
        leg=a[i][n-1-i]
    return leg






