
class Skrit:
    def __init__(self, input):
        self._SAMOGLASNICI = ['a','e','i','o','u','r','A','E','I','O','U','R']
        self._SERBIAN_BLETTERS = [['l','j'],['n','j'],['s','h'],['d','j'],['d','z'],['d','ž'],'ž']
        self._input = input
        self._output = self.Satrovacki(self._input)
    def __str__(self) -> str:
        return str(self._output)
    def isOdd(self,x):
        return x % 2
    def isSamoglasnik(self,x):
        for l in self._SAMOGLASNICI:
            return x.find(l) > 0
        return False
    def Satrovacki(self, input):
        l = list(input)
        cl = len(l)
        hl = round(cl/2)
        par = self.isOdd(cl)
        # print(l)
        # print("cl: "+str(cl))
        # print("hl: "+str(hl))
        # print("par: "+str(par))
        output = ""
        while hl < cl:
            output += input[hl]
            hl += 1
        i = 0
        while i < hl:
            output += input[i]
            i += 1
        return output

print(Skrit('rucka'))


