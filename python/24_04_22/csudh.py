class Domain:
    def __init__(self,name, ip):
        self.name = name
        self.ip = ip

lista = []
def beolvas():
    f = open("csudh.txt",encoding="UTF-8")
    f.readline()
    for sor in f:
        reszek = sor.strip().split(';')
        name = reszek[0]
        ip = reszek[1]
        obj = Domain(name, ip)
        lista.append(obj)
    f.close()
    
def fel_3():
    print(f"3. feladat: Domainek száma: {len(lista)}")

def fel_4(nev):
    van = False
    for item in lista:
        if item.name == nev:
            van = True
            levels = item.name.split(".")
            for i in range(5-(len(levels))):
                levels.insert(0,"nincs")
            return levels    
    if van == False:
        return"nincs"
                
def fel_5():
    print(f"5. feladat: Az első domain felépítése: ")
    dom = fel_4("dhvx20.csudh.edu")
    c = 0
    for i in range(5,0,-1):
        print(f"\t{c+1}. szint: {dom[i-1]}")
        c += 1


def main():
    beolvas()
    fel_3()
    fel_5()
main()