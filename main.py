from math import *

class Main:
    def __init__(self):
        while True:
            print("\n--------------------------------------------------------------------------\n")
            print("Selecione o que você tem: ")
            classe = input("Digite de (0-4)\nN = 0 \nEmissão = 1 \nAbsorção = 2 \nFótons = 3 \nSair = 4\n")
            if classe == "0":
                N()
            elif classe == "1":
                Emissao()
            elif classe == "2":
                Absorcao()
            elif classe == "3":
                Fotons()
            else:
                break

# ev para joule = *
# Joule para ev = /
class N:
    def __init__(self):
        self.c = 3*(10**8)
        self.hev = 4.136e-15
        self.hj = 6.626e-34
        self.m = 9.11e-31
        self.converterEvJ = 1.602e-9
        self.n = int(input("Digite o N: "))
        print("\n--------------------------------------------------------------------------\n")
        self.converterParaRaio()
        self.converterParaVelocidade()
        self.converterParaECinetica()
        self.converterParaEPotencial()
        self.converterParaEtotal()
        self.converterParaCondaB()

    def converterParaRaio(self):
        self.raio = (self.n*self.n) * 5.29e-11
        print(f"Raio da órbita: {self.raio:.2e} m\t ou \t {1e9*self.raio:.2e} nm")  # Notação científica com 3 numeros significativos

    def converterParaVelocidade(self):
        self.velocidade = 2.187e6/self.n
        print(f"Velocidade: {self.velocidade:.2e} m/s")  # Notação científica com 3 numeros significativos

    def converterParaECinetica(self):
        self.eCinetica = 13.6/(self.n*self.n)
        print(f"Energia Cinética: {self.eCinetica:.2e} eV")  # Notação científica com 3 numeros significativos
    
    def converterParaEPotencial(self):
        self.epotencial = -27.2/(self.n*self.n)
        print(f"Energia Potencial: {self.epotencial:.2e} eV")  # Notação científica com 3 numeros significativos

    def converterParaEtotal(self):
        self.etotal = -13.6/(self.n*self.n)
        print(f"Energia Total: {self.etotal:.2e} eV")  # Notação científica com 3 numeros significativos

    def converterParaCondaB(self):
        self.condab = self.hj/(self.velocidade * self.m) 
        print(f"Comprimento de onda De Broglie do eletron: {self.condab:.2e} m\t ou \t {1e9*self.condab:.2e} nm")  # Notação científica com 3 numeros significativos

class Emissao:
    def __init__(self):
        self.c = 3*(10**8)
        self.menu()
        print("\n--------------------------------------------------------------------------\n")

    def menu(self):
        self.c = 3*(10**8)
        self.hev = 4.136e-15
        self.hj = 6.626e-34
        self.m = 9.11e-31
        self.converterEvJ = 1.602e-9
        print("\n--------------------------------------------------------------------------\n")
        print("Selecione o que você tem: ")
        classe = input("Digite de (0-6)\nNi e Frequência = 0 \nNi e Comprimento de onda = 1 \nNf e Frequência = 2 \nNf e Comprimento de onda = 3 \nNf e Ni = 4\n")
        if classe == "0":
                self.freq = float(input("Digite a frequência (em THz): "))
                self.ni = int(input("Digite o n inicial: "))
                self.emitConverterDeFreqeNi()

        elif classe == "1":
                self.conda = float(input("Digite o comprimento de onda (em nm): "))
                self.ni = int(input("Digite o n inicial: "))
                self.emitConverterDeCondaeNi()

        elif classe == "2":
                self.freq = float(input("Digite a frequência (em THz): "))
                self.nf = int(input("Digite o n final: "))
                self.emitConverterDeFreqeNf()

        elif classe == "3":
                self.conda = float(input("Digite o comprimento de onda (em nm): "))
                self.nf = int(input("Digite o n final: "))
                self.emitConverterDeCondaeNf()

        elif classe == "4":
                self.ni = int(input("Digite o n inicial: "))
                self.nf = int(input("Digite o n final: "))
                self.emitConverterParaEfoton()
                self.emitConverterParaCondaf()
                self.emitConverterParaFrequenciaf()
            
        
    def emitConverterParaEfoton(self):
        self.eFotonemit = (-13.6/(self.ni * self.ni))-(-13.6/(self.nf * self.nf))
        print(f"Energia do fóton emitido: {self.eFotonemit:.2e} eV")  # Notação científica com 3 numeros significativos
    
    def emitConverterParaCondaf(self):
        self.condafa = (self.hev * self.c) / self.eFotonemit
        print(f"Comprimento de onda do fóton emitido: {self.condafa:.2e} m\t ou \t {1e9*self.condafa:.2e} nm")  # Notação científica com 3 numeros significativos

    def emitConverterParaFrequenciaf(self):
        self.frequenciafa =  self.eFotonemit / self.hev
        print(f"Frequência do fóton emitido: {self.frequenciafa:.2e} Hz\t ou \t {1e-12*self.frequenciafa:.2e} THz")  # Notação científica com 3 numeros significativos

    def emitConverterDeFreqeNf(self):
        self.eFoton = self.hev * (self.freq * 1e12)
        self.eInicial = self.eFoton + (-13.6/(self.nf * self.nf))
        self.ni = sqrt((-13.6)/self.eInicial)
        print(f"N inicial: {self.ni:.2e}")  # Notação científica com 3 numeros significativos
    
    def emitConverterDeCondaeNf(self):
        self.eFoton = (self.hev * self.c) / (self.conda / 1e9)
        self.eInicial = self.eFoton + (-13.6/(self.nf * self.nf))
        self.ni = sqrt((-13.6)/self.eInicial)
        print(f"N inicial: {self.ni:.2e}")  # Notação científica com 3 numeros significativos

    def emitConverterDeFreqeNi(self):
        self.eFoton = self.hev * (self.freq * 1e12)
        self.eFinal = (-13.6/(self.ni * self.ni)) - self.eFoton
        self.nf = sqrt((-13.6)/self.eFinal)
        print(f"N final: {self.nf:.2e}")  # Notação científica com 3 numeros significativos
    
    def emitConverterDeCondaeNi(self):
        self.eFoton = (self.hev * self.c) / (self.conda / 1e9)
        self.eFinal = (-13.6/(self.ni * self.ni)) - self.eFoton
        self.nf = sqrt((-13.6)/self.eFinal)
        print(f"N final: {self.nf:.2e}")  # Notação científica com 3 numeros significativos

class Absorcao:
    def __init__(self):
        self.c = 3*(10**8)
        self.menu()
        
        
        print("\n--------------------------------------------------------------------------\n")

    def menu(self):
        self.c = 3*(10**8)
        self.hev = 4.136e-15
        self.hj = 6.626e-34
        self.m = 9.11e-31
        self.converterEvJ = 1.602e-9
        print("\n--------------------------------------------------------------------------\n")
        print("Selecione o que você tem: ")
        classe = input("Digite de (0-6)\nNi e Frequência = 0 \nNi e Comprimento de onda = 1 \nNf e Frequência = 2 \nNf e Comprimento de onda = 3 \nNf e Ni = 4\n")
        if classe == "0":
                self.freq = float(input("Digite a frequência (em THz): "))
                self.ni = int(input("Digite o n inicial: "))
                self.absConverterDeFreqeNi()

        elif classe == "1":
                self.conda = float(input("Digite o comprimento de onda (em nm): "))
                self.ni = int(input("Digite o n inicial: "))
                self.absConverterDeCondaeNi()
                
        elif classe == "2":
                self.freq = float(input("Digite a frequência (em THz): "))
                self.nf = int(input("Digite o n final: "))
                self.absConverterDeFreqeNf()

        elif classe == "3":
                self.conda = float(input("Digite o comprimento de onda (em nm): "))
                self.nf = int(input("Digite o n final: "))
                self.absConverterDeCondaeNf()

        elif classe == "4":
                self.ni = int(input("Digite o n inicial: "))
                self.nf = int(input("Digite o n final: "))
                self.absConverterParaEfoton()
                self.absConverterParaCondafa()
                self.absConverterParaFrequenciafa()

    def absConverterParaEfoton(self):
        self.eFoton = (-13.6/(self.nf * self.nf))-(-13.6/(self.ni * self.ni))
        print(f"Energia do fóton absorvido: {self.eFoton:.2e} eV")  # Notação científica com 3 numeros significativos
    
    def absConverterParaCondafa(self):
        self.condafa = (self.hev * self.c) / self.eFoton
        print(f"Comprimento de onda do fóton absorvido: {self.condafa:.2e} m\t ou \t {1e9*self.condafa:.2e} nm")  # Notação científica com 3 numeros significativos

    def absConverterParaFrequenciafa(self):
        self.frequenciafa =  self.eFoton / self.hev
        print(f"Frequência do fóton absorvido: {self.frequenciafa:.2e} Hz\t ou \t {1e-12*self.frequenciafa:.2e} THz")  # Notação científica com 3 numeros significativos

    def absConverterDeFreqeNi(self):
        self.eAbs = self.hev * (self.freq * 1e12)
        self.eFinal = (-13.6/(self.ni * self.ni)) + self.eAbs
        self.nf = sqrt((-13.6)/self.eFinal)
        print(f"N final: {self.nf:.2e}")  # Notação científica com 3 numeros significativos
    
    def absConverterDeCondaeNi(self):
        self.eAbs = (self.hev * self.c) / (self.conda / 1e9)
        self.eFinal = (-13.6/(self.ni * self.ni)) + self.eAbs
        self.nf = sqrt((-13.6)/self.eFinal)
        print(f"N final: {self.nf:.2e}")  # Notação científica com 3 numeros significativos
    
    def absConverterDeFreqeNf(self):
        self.eAbs = self.hev * (self.freq * 1e12)
        self.eInicial = (-13.6/(self.nf * self.nf)) - self.eAbs
        self.ni = sqrt((-13.6)/self.eInicial)
        print(f"N inicial: {self.ni:.2e}")  # Notação científica com 3 numeros significativos
    
    def absConverterDeCondaeNf(self):
        self.eAbs = (self.hev * self.c) / (self.conda / 1e9)
        self.eInicial = (-13.6/(self.nf * self.nf)) - self.eAbs
        self.ni = sqrt((-13.6)/self.eInicial)
        print(f"N inicial: {self.ni:.2e}")  # Notação científica com 3 numeros significativos


class Fotons:
    def __init__(self):
        self.menu()
        print("\n--------------------------------------------------------------------------\n")

    def menu(self):
        self.c = 3*(10**8)
        self.hev = 4.136e-15
        self.hj = 6.626e-34
        self.m = 9.11e-31
        self.converterEvJ = 1.602e-19
        print("\n--------------------------------------------------------------------------\n")
        print("Selecione o que você tem: ")
        classe = input("Digite de (0-2)\nComprimento de Onda = 0 \nFrequência = 1 \nEnergia = 2 \n")
        if classe == "0":
                self.conda = float(input("Digite o comprimento de onda (em nm): "))
                self.fotonConverterDeConda()
        elif classe == "1":
                self.freq = float(input("Digite a frequência (em Hz): "))
                self.fotonConverterDeFreq()
        elif classe == "2":
                escolha = input("Escreva 'eV' ou 'Joule' para converter: ")
                if escolha == "eV":
                    self.menorEnergia = float(input("Digite a menor energia (em eV): "))
                    self.maiorEnergia = float(input("Digite a maior energia (em eV): "))
                    self.fotonConverterDeEnergiaEv()
                elif escolha == "Joule":
                    self.menorEnergia = float(input("Digite a menor energia (em Joule): "))
                    self.maiorEnergia = float(input("Digite a maior energia (em Joule): "))
                    self.fotonConverterDeEnergiaJ()


    def fotonConverterDeConda(self):
        self.eVFoton = (self.hev * self.c) / (self.conda / 1e9)
        self.JFoton = self.eVFoton * self.converterEvJ
        print(f"Energia: {self.JFoton:.2e} J")  # Notação científica com 3 casas decimais
        print(f"Energia: {self.eVFoton:.2e} eV")  # Notação científica com 3 casas decimais

    def fotonConverterDeFreq(self):
        self.JFoton = self.hj * self.freq 
        self.eVFoton = self.JFoton / self.converterEvJ
        print(f"Energia: {self.JFoton:.2e} J")  # Notação científica com 3 casas decimais
        print(f"Energia: {self.eVFoton:.2e} eV")  # Notação científica com 3 casas decimais

    def fotonConverterDeEnergiaEv(self):
        self.maiorConda = (self.hev * self.c) / self.menorEnergia
        self.menorConda = (self.hev * self.c) / self.maiorEnergia
        print(f"Menor comprimento: {self.menorConda:.2e} m\t ou \t {1e9*self.menorConda:.2e} nm")  # Notação científica com 3 casas decimais
        print(f"Maior comprimento: {self.maiorConda:.2e} m\t ou \t {1e9*self.maiorConda:.2e} nm")  # Notação científica com 3 casas decimais

        self.maiorFreq = self.c / self.menorConda
        self.menorFreq = self.c / self.maiorConda
        print(f"Menor frequência: {self.menorFreq:.2e} Hz")  # Notação científica com 3 casas decimais
        print(f"Maior frequência: {self.maiorFreq:.2e} Hz")  # Notação científica com 3 casas decimais
    
    def fotonConverterDeEnergiaJ(self):
        self.maiorFreq = self.maiorEnergia / self.hj
        self.menorFreq = self.menorEnergia / self.hj

        self.maiorConda = self.c / self.menorFreq
        self.menorConda = self.c / self.maiorFreq

        print(f"Menor comprimento: {self.menorConda:.2e} m\t ou \t {1e9*self.menorConda:.2e} nm")  # Notação científica com 3 casas decimais
        print(f"Maior comprimento: {self.maiorConda:.2e} m\t ou \t {1e9*self.maiorConda:.2e} nm")  # Notação científica com 3 casas decimais
        print(f"Menor frequência: {self.menorFreq:.2e} Hz")  # Notação científica com 3 casas decimais
        print(f"Maior frequência: {self.maiorFreq:.2e} Hz")  # Notação científica com 3 casas decimais 
        

if __name__ == '__main__':
    print("Autores: Aline Rocha de Jesus, Arthur Carvalho Rotkis, Bianca Silva Oliveira")
    print("O objetivo deste projeto é demonstrar, por meio de um código Python, as ondas eletromagnéticas,\nque são ondas capazes de propagar no vácuo e de se formarem pela combinação entre os campos elétricos e magnéticos,\nque são responsáveis pela onda de rádio, micro-ondas, infravermelho, luz visível, raios ultravioletas, raio X e raios gama.\nAlém disso, as ondas eletromagnéticas são classificadas de acordo com a frequência, oscilação e comprimento de onda, que também são representados dentro do código.")
    
    app = Main()

