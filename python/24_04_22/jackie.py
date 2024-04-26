import datetime
class Statisztika:
    def __init__(self,year,	races	,wins	,podiums,	poles,	fastests):
        try:
            self.year = int(year)
        except:
            self.year = None
        self.races = races
        try:
            self.wins = int(wins)
        except:
            self.wins = None
        self.podiums = podiums
        self.poles = poles
        self.fastests = fastests

lista = []
s = ""
def beolvas():
    f = open("jackie.txt",encoding="UTF-8")
    f.readline()
    for sor in f:
        reszek = sor.strip().split("\t")
        obj = Statisztika(reszek[0],reszek[1],reszek[2],reszek[3],reszek[4],reszek[5])
        lista.append(obj)
    f.close()

def fel_3():
    print(f"3. feladat: {len(lista)}")

def fel_4():
    legt = lista[0].races
    for item in lista:
        if item.races > legt:
            legt = item.races
    
    for item in lista:
        if legt == item.races:
            print(f"4. feladat: {item.year}")

def fel_5():
    print(f"5. feladat: ")
    print(f"\t 70-es évek:", end="")
    megnyertek = 0
    for item in lista:
        if item.year >= 1970 and item.year <=1979:
            megnyertek += item.wins
    print(f"{megnyertek} megnyert versenyek")

    megnyertek = 0
    print(f"\t 60-es évek:", end="")
    for item in lista:
        if item.year >= 1960 and item.year <=1969:
            megnyertek += item.wins
    print(f"{megnyertek} megnyert versenyek")

def fel_6():
    print(f"6. feladat: ")
    global s 

    f = open("jackie.html","w",encoding="UTF-8")
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n')
    f.write('<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Document</title>\n')
    f.write('</head>>\n')
    
    f.write("<body>\n")
    
    f.write("<table>")
    for item in lista:
        f.write(f"<tr><td>{item.year}</td><td>{item.races}</td><td>{item.wins}</td></tr>\n")
    f.write("</table>\n")
    f.write("</body>\n")
    f.write("</html>\n")
    f.close()
    
def main():
    beolvas()
    fel_3()
    fel_4()
    fel_5()
    fel_6()
main()