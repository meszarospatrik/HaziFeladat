
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
            
    
    
    def feladat_11():
    try:
        fajl=open("be.txt",mode="r")
        hossz=0
        sor=fajl.readline()
        for sor in fajl:
            sor=sor.strip()
            hossz=hossz+1                       #Folyamatban van
        if  sor==2




def feladat_17():
    try:
        fajl1=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        sor=fajl1.readline()
        for sor in fajl1:
            if sor.islower():
                fajl2.write("%d %d" % (sor))

        fajl2.close()
        fajl1.close()

    except Exception as e:
        print(e)
        
        
        
 




def feladat_16():
    try:
        fajl=open("be.txt", mode="r")
        fajl2=open("ki.txt", mode="w")
        sor=fajl.readline()
        for sor in fajl:
            if sor.isupper():
                fajl2.write("%d %d" % (sor))

        fajl2.close()
        fajl.close()

    except Exception as e:
        print(e)
        
        
        
        
        
def feladat_15():
    try:
        fajl=open("be.txt", mode="r")                          #Megoldásra vár
        fajl2=opem("Ki.txt",mode="W")
        sor=fajl.readline()
        if sor=="":
            sor.split()
        fajl2.write("%d %d" % (sor))
        fajl.close()
        fajl2.close()

    except Exception as e:
        print(e)



        
def feladat_19():
    try:
        fajl=open("be.txt",mode="r")
        legtobb=()

        for sor in fajl:
            sor=sor.strip()
            legtobb=max(sor)

        return legtobb
        fajl.close()

    except Exception as e:
        print(e)




def feladat_20():
    try:
        fajl=open("be.txt",mode="r")
        sor=fajl.readline()
        for sor in fajl:
            sor=sor.strip()
            x=sor.split(";")
            legtobb=int(x[0])
            leg=max(legtobb)

        return leg
        fajl,close()

    except Exception as e:
        print(e)



        
def feladat_21():
    try:                                                        #módosítás alatt
        fajl=open("be.txt",mode="r")
        fajl1=open("ki.txt",mode="w")
        sor=fajl.readline()
        for sor in fajl:
            x=sor.split(";")
            pilota=int(x[0])
            sum1=sum(pilota)

        fajl1.write("%d %d" % ((pilota))
        fajl.close()
        fajl1.close()

    except Exception as e:
        print(e)

















