import math as mt

def feladat_1(a,b):
    a=a+b
    b=a-b
    a=a-b

    print(a,b)



def feladat_2():
    a=int(input("Adj meg egy egész számot:"))
    b=int(input("Adj meg még egy egész számot:"))
    c=int(input("Adj meg egy harmadik egész számot:"))
    lista=[a,b,c]
    lista.sort()
    print(lista)



def feladat_3(x):
    if x>-2 and x<2:
        return 2*x
    elif x>=0 and x<2:
        return x*x
    elif x>2:
        return 10
    else:
        print("A fuggveny nem ertelmezett!")
        return



def feladat_6():
    while True:
        a=float(input("A haromszog oldalai:"))
        b=float(input("A haromszog oldalai:"))
        c=float(input("A haromszog oldalai:"))
        if a<=0 or b<=0 or c<=0:
            print("Nem megfelelo adatok!")
        else:
            break
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        T=mt.sqrt(p*(p-a)*(p-b)*(p-c))
        r=T/p
        R=a*b*c/(4*T)
        print("R=%.2f és r=%.2f" % (R,r))
    else:
        print("Nem kepezhetik!")




def feladat_7(a,b,n):
    k=(a+b)*2
    if k==n:
        return print("Pont elég")
    elif k<n:
        return n-k
    elif k>n:
        return k-n



def feladat_19(n):
    prim=True
    if n==1:
        prim=False

    for i in range(2,int(mt.sqrt(n))+1):
        if n%i==0:
            prim = False
            break
    return prim
