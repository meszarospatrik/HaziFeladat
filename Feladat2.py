
def feladat_9():
    n=1
    k=1
    x=0
    for i in range():
        k+(1/n+1)
        x+=1
        if k==300:
            return print(x)

        
        
        
        
def feladat_10():
    try:
        fajl=open(fajl_nev,mode="r")
        betuk=string.split(fajl)
        betukszama=0
        for i in range(len(fajl)):
            if fajl.isupper():
                for i in betuk:
                    betukszama += len(i)
        return betukszama
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()


def osztok_szama(szam):
    db=2
    for i in range(2,szam//2+1):
        if szam%i==0:
            db=db+1

    return db



def feladat_5(n):
    max=1
    for i in range(2,n+1):
        if max<osztok_szama(i):
            max=osztok_szama(i)
            print(i)
            
            
            
   def feladat_15():
    try:
        fajl1=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        sor=fajl1.readline()
        if bool(sor)==False:
            sor=sor.strip()
        else:
            return sor
        fajl2.write("%d","%d" % (sor))
        fajl1.close()
        fajl2.close()

    except Exception as e:
        print(e)         
            
    



































