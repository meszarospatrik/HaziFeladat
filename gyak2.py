def fibo(n):
    a=1
    b=1
    if n==1:
        print(a,end=" ")
    elif n==2:
        print(a,b,end=" ")
    else:
        c=a+b
        print(a,b,c,end=" ")
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c,end=" ")
            k+=1

def fibo2(n):
    a=1
    b=1
    k=1
    fajl=open("ki1.txt",mode="w")
    while k<n:
        #print("%.4f" % (a/b),end=" ")
        fajl.write("%.4f " % (a/b))
        a=a+b
        b=a-b
        k=k+1

    fajl.close()

def csere():
    a=a+b
    b=a-b
    a=a-b

    print(a,b)

import codecs as cod
def feladat1(fajl_nev):
    fajl=cod.open(fajl_nev,encoding='utf-8', mode="r")
    max=0
    max_sor=""
    for sor in fajl:
        sor=sor.strip()
        if(sor[0].isupper() and len(sor)>max):
            max=len(sor)
            max_sor=sor
    print(max,max_sor)
    fajl.close()



def feladat2():
    fajl=open("be1.txt",mode="r")
    for sor in fajl:
        if("   "in sor):
            fajl=open("ki1.txt",mode="w")
            fajl.write(sor)
            fajl.close()
            break


def feladat7(lista,betű):
    li=[]
    fajl=open("ki2.txt", mode="w")
    for i in lista:
        if i[0]==betű:
            li.append(i)
    fajl.write(str(li))
    fajl.close()

















def main():
    feladat7(["alma", "ananasz", "narancs"],'a')


if __name__ == "__main__":
    main()