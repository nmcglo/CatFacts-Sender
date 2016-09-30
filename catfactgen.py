import random

class catfactgenerator:

    def __init__(self):
        self.usedfacts = set()

        sourcefile = open("catfacts.txt", 'r')
        catdict = {}
        i = 1
        for line in sourcefile:
            catdict[i] = line.rstrip()
            i += 1
        self.catdict = catdict
        self.waittime = 900
        self.numfactsused = 0


    def getfact(self):
        poschoice = random.randint(1,len(self.catdict))
        while(poschoice in self.usedfacts):
            poschoice = random.randint(1,len(self.catdict))
            if(len(self.usedfacts) == len(self.catdict)):
                break
            # print('AVOIDED COLLISION')

        response = 'CatFact (%i): '%poschoice
        response += self.catdict[poschoice]

        self.usedfacts.add(poschoice)
        self.numfactsused += 1

        return response