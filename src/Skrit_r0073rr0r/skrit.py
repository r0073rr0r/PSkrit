class skrit:
    def __init__(self):
        self._SAMOGLASNICI = ['a','e','i','o','u','r','A','E','I','O','U','R']
        self._SERBIAN_LETTERS = [['l','j'],['n','j'],['s','h'],['d','j'],['d','z'],['d','ž'],'ž','']
    def __call__(self,input):
        return self.Satrovacki(input)
    def __str__(self) -> str:
        return str(self._output)
    def isOdd(self,x):
        return x % 2
    def isSamoglasnik(self,x):
        for l in self._SAMOGLASNICI:
            return x.find(l) > 0
        return False
    def isSerbianLetter(self,x):
        for l in self._SAMOGLASNICI:
            return x.find(l) > 0
        return False        
    def Satrovacki(self, input):
        l = list(input)
        cl = len(l)
        hl = round(cl/2)
        par = self.isOdd(cl)
        #print({"L:": l, "Length": str(cl), "Half": str(hl),"Pair": str(par), "LastInHalf": str(l[hl])})
        # @TODO samoglasnici and serbian letters to parse: pishtolj or pištolj as štoljpi or shtoljpi
        output = input[hl:cl]
        output += input[0:hl]
        return output