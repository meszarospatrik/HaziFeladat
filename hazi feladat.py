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




def feladat_10(ev1,ev2):
    db=0
    for i in range(ev1,ev2+1):
        if i%4==0 or i%400==0:
            db+=1
        elif i%100==0:
            return 0
    print(db)





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

