import math as mt

def feladat_1(a,b):
    a=a+b
    b=a-b
    a=a-b



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


def feladat_4(a,b,c):
    lista=[a,b,c]
    mini=min(lista)
    maxi=max(lista)
    return mini,maxi


def feladat_5(a,b,c,d):
    print(a,b,c,d)
    if d>=0:
        c=c+b
        b=c-b
        c=c-b
        print(a,b,c,d)
    else:
        d=d+c
        c=d-c
        d=d-c
        print(a,b,c,d)





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

def feladat_8(x,a,b,c,d):
    if x<5:
        return 3*x-5
    elif x>=5 and x<=10:
        return 10
    elif x>10:
        return 9*x-1
    else:
        print("A függvény nem értelmezett.")

    if a+c>2*d and b>0:
        return d-3*b
    elif a+c<2*d and b<0:
        return d+3*b
    else:
        return 4


def feladat_9(a,b,c):
    d=b*b-(4*a*c)
    if d>0:
        e=math.sqrt(d)
        k1=float(-b+e)/(2*a)
        k2=float(-b-e)/(2*a)
        print("A gyökök:" ,k1,k2)
    else:
        print("Komplex gyökök")




def feladat_10(ev1,ev2):
    db=0
    for i in range(ev1,ev2+1):
        if i%4==0 or i%400==0:
            db+=1
        elif i%100==0:
            return 0
    return db





def feladat_11():
    print("Adja meg a születési dátumát.")
    x = input("Év: ")
    y = input("Hónap (1-12): ")
    k = input("Nap: ")

    from datetime import date

    ma = date.today()

    szuletesnap = date(int(x),int(y),int(k))

    nap = ma - szuletesnap

    print("Ennyi napot élt a mai napig: %s" % nap)





def feladat_12(a,b):
    if (b/a)>=0.6:
        print("A dolgozat sikeres.")
    else:
        print("A dolgozat sikertelen.")








def feladat_13():
    jegy=int(input("Írja be az érdemjegyet:"))
    if jegy==5:
        print("Jeles")
    elif jegy==4:
        print("Jó")
    elif jegy==3:
        print("Közepes")
    elif jegy==2:
        print("Elégséges")
    elif jegy==1:
        print("Elégtelen")
    else:
        print("Nem megfelelő értéket adott meg.")



def feladat_14():
    honap=int(input("Adja meg valamelyik hónap sorszámát:"))
    if honap==1:
        print("január")
    elif honap==2:
        print("február")
    elif honap==3:
        print("március")
    elif honap==4:
        print("április")
    elif honap==5:
        print("május")
    elif honap==6:
        print("június")
    elif honap==7:
        print("július")
    elif honap==8:
        print("augusztus")
    elif honap==9:
        print("szeptember")
    elif honap==10:
        print("oktober")
    elif honap==11:
        print("november")
    elif honap==12:
        print("december")
    else:
        print("Nem megfelelő formátum.")




def feladat_15(a,b):

    hanyados=0
    while a>=b:
        hanyados=+1
        a=a-b

    print(hanyados)






def feladat_16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return a


def feladat_17(n):
    masolat=n
    uj_szam=0
    while n!=0:
        szj=n%10
        uj_szam=uj_szam*10+szj
        n=n//10

    return uj_szam==masolat



def feladat_18(a,b):
    x=a
    y=b
    p=0
    while x>0:
        if x%2!=0:
            p=p+y
        x=x/2
        y=y+y
        break
    return p





def feladat_19(n):
    prim=True
    if n==1:
        prim=False

    for i in range(2,int(mt.sqrt(n))+1):
        if n%i==0:
            prim = False
            break
    return prim



def feladat_20(n):
    a=1
    b=1
    k=1

    while k<n:
        print("%.4f" % (a/b),end=" ")

        a=a+b
        b=a-b
        k=k+1




def feladat_21(n):
    d=0
    ujszam=0
    while (n>0):
        d=n%10
        n=int(n/10)
        ujszam=ujszam*10+d

    return (ujszam)



def feladat_22(x,n):
    eredmeny=x**n
    return eredmeny






def feladat_23(n):

    szam=0
    for i in range(1,n):
        if(n%i)==0:
            szam=szam+i
    if szam==n:
        return "Tökéletes szám"
    else:
        return "Nem tökéletes"







def feladat_25():
    x=int(input("Ország lakosainak a száma:"))
    y=int(input("Ország területe:"))
    a=x/y
    print("Az ország népsűrűsége %s" %a)
    if a<50:
        print("Az ország ritkán lakott.")
    elif 50<=a<300:
        print("Az ország átlagos népsűrűségű.")
    else:
        print("Az ország sűrűn lakott.")



def feladat_29(n):
    szam=1
    for i in range(n):
        szam=szam*(i+1)
    return szam




def feladat_30():
    print("Adjon meg egy dátumot dátumát.")
    x = input("Év: ")
    y = input("Hónap (1-12): ")
    k = input("Nap: ")

    from datetime import date
    ev=date(int(x),1,1)
    datum = date(int(x),int(y),int(k))

    nap = (ev-datum)*-1

    print(nap)




def feladat_31(n):
    osztok = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                osztok.append(n/i)
    for osztok1 in reversed(osztok):
        yield osztok1



def feladat_32(k):
    n1=int(input("Adjon meg egy számot."))
    n2=int(input("Adjon meg egy másik számot."))
    lista=[]
    for i in range(n1,n2):
        if i%k==0:
            lista.append(i)
    return lista








def main():
    feladat_1(1,5)
    feladat_2()
    feladat_3(3)
    feladat_4(10,30,40)
    feladat_5(1,2,3,4)
    feladat_6()
    feladat_7(5,6,30)
    feladat_8(2,5,4,6,8)
    feladat_9(5,6,8)
    feladat_10(2000,2010)
    feladat_11()
    feladat_12(100,60)
    feladat_13()
    feladat_14()
    feladat_15(10,5)
    feladat_16(5,7)
    feladat_17(40)
    feladat_18(10)
    feladat_19(7)
    feladat_20(5)
    feladat_21(321)
    feladat_22(5,7)
    feladat_23(10)
    feladat_25()
    feladat_29(6)
    feladat_30()
    feladat_31(100)
    feladat_32(2)
    


if __name__=="__main__":
    main()
