import datetime
class Versenyzo:
    def __init__(self,nev,szuletes,nemzetiseg,rajtszam):
        self.nev = nev
        self.szuletes = szuletes
        self.nemzetiseg = nemzetiseg
        try:
            self.rajtszam = int(rajtszam)
        except:
            self.rajtszam = None

lista = []
def beolvas():
    f = open("pilotak.csv",encoding="UTF-8")
    f.readline()
    for sor in f:
        reszek = sor.strip().split(';')
        nev = reszek[0]
        format = "%Y.%m.%d"
        datum = datetime.datetime.strptime(reszek[1], format)
        nemzetiseg = reszek[2]
        rajtszam = reszek[3]
        obj = Versenyzo(nev,datum,nemzetiseg,rajtszam)
        lista.append(obj)
    f.close()

def fel_3():
    print(f"3. feladat: {len(lista)}")

def fel_4():
    for item in lista:
        utso = item
    print(f"4. feladat: {utso}")

def fel_5():
    print(f"5. feladat:")
    for item in lista:
        if item.szuletes < datetime.datetime(1901,1,1):
            print(f"\t{item.nev} ({item.szuletes})")

def fel_6():
    target_set = [x for x in lista if x.rajtszam]
    smallest = min(target_set, key=lambda pilota: pilota.rajtszam)

    print(f"6. feladat: {smallest.nemzetiseg}")
    
def fel_7():
    print("7. feladat:",end="")
    dict={}
    for item in lista:
        kulcs=item.rajtszam
        if kulcs not in dict:
            dict[kulcs]=0
        dict[kulcs]+=1
    for item in dict:
        if dict[item]>=2:
            print(item,end=', ')  

def main():
    beolvas()
    fel_3()
    fel_4()
    fel_5()
    fel_6()
    fel_7()
main()