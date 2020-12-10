import random
import os

file = open(os.path.dirname(os.path.abspath(__file__)) + "\\szabalyok.txt",encoding="utf8")
file.readline()
terminalis = (file.readline().strip().split(","))
file.readline()
nemterminalis = (file.readline().strip().split(","))
file.readline()
kezdo = file.readline().strip()
file.readline()
szabalyok = []
while True:
    try:
        a = file.readline().strip().split("->")
        if a[0]=="":
            break
        szabalyok.append(a)
    except Exception as error:
        print(error)
        break

def findTerminalis(s):
    for t in terminalis:
        if s.find(t)>=0:
            return t
    return False

def getRandomCsere(termin):
    corrszabalyok = []
    for szab in szabalyok:
        if szab[0]==termin:
            corrszabalyok.append(szab)
    return random.choice(corrszabalyok)

def getOutput(steps):
    string = kezdo
    for i in range(steps):
        selectedTerminalis = findTerminalis(string)
        if not(selectedTerminalis):
            return string
        randomcsere = getRandomCsere(selectedTerminalis)
        if randomcsere[1]=="E":
            randomcsere[1] = ""
        string = string.replace(randomcsere[0],randomcsere[1],1)
        #print(string)
    return string

for i in range(20):
    print(getOutput(1000))
