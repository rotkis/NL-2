from math import *

class Main:
    def __init__(self):
        while True:
            print("\n--------------------------------------------------------------------------\n")
            print("Selecione o que você tem: ")
            classe = input("Digite de (0-6)\nN = 0 \nEmissão = 1 \nAbsorção = 2 \nFótons = 3 \nSair = 4\n")
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
        print(f"Raio da órbita: {self.raio:.2e} m\t{1e9*self.raio:.2e} nm")  # Notação científica com 3 numeros significativos

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
        print(f"Comprimento de onda De Broglie do eletron: {self.condab:.2e} m\t{1e9*self.condab:.2e} nm")  # Notação científica com 3 numeros significativos

class Emissao:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * 3.14) * (10 ** -7)
        self.cMagnetico = float(input("Digite o campo magnético (em T): "))
        print("\n--------------------------------------------------------------------------\n")
        self.converterParaCampoEletrico()
        self.converterParaIntesidade()

    def converterParaCampoEletrico(self):
        self.cEletrico = self.c * self.cMagnetico
        print(f"Campo Elétrico: {self.cEletrico:.3e} V/m")  # Notação científica com 3 casas decimais

    def converterParaIntesidade(self):
        self.Intesidade = (self.c * (self.cMagnetico ** 2)) / (2 * self.mi)
        print(f"Intensidade: {self.Intesidade:.3e} W/m²")  # Notação científica com 3 casas decimais

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
                pass
        elif classe == "1":
                Emissao()
        elif classe == "2":
                Absorcao()
        elif classe == "3":
                Fotons()
        elif classe == "4":
                self.ni = int(input("Digite o n inicial: "))
                self.nf = int(input("Digite o n final: "))
                self.converterParaEfoton()
                self.converterParaCondafa()
                self.converterParafrequenciafa()
            
        

    def converterParaEfoton(self):
        self.eFoton = (-13.6/(self.nf * self.nf))-(-13.6/(self.ni * self.ni))
        print(f"Energia do foton: {self.eFoton:.2e} eV")  # Notação científica com 3 numeros significativos
    
    def converterParaCondafa(self):
        self.condafa = (self.hev * self.c) / self.eFoton
        print(f"Comprimento de onda do foton absorvido: {self.condafa:.2e} m\t{1e9*self.condafa:.2e} nm")  # Notação científica com 3 numeros significativos

    def converterParafrequenciafa(self):
        self.frequenciafa =  self.eFoton / self.hev
        print(f"frequência do foton absorvido: {self.frequenciafa:.2e} Hz\t{1e-12*self.frequenciafa:.2e} THz")  # Notação científica com 3 numeros significativos



class Fotons:
    def __init__(self):
        self.c = 3*(10**8)
        self.mi = (4 * pi) * (10 ** (-7))
        self.intensidade = float(input("Digite a Intensidade (em W/m²): "))
        print("\n--------------------------------------------------------------------------\n")
        self.converterParaCampoEletrico()
        self.converterParaCampoMag()


    def converterParaCampoEletrico(self):
        self.cEletrico = sqrt(self.intensidade * 2 * self.mi * self.c)
        print(f"Campo Elétrico: {self.cEletrico:.3e} V/m")  # Notação científica com 3 casas decimais

    def converterParaCampoMag(self):
        self.cMagnetico = sqrt((self.intensidade * 2 * self.mi) / self.c)
        print(f"Campo Magnético: {self.cMagnetico:.3e} T")  # Notação científica com 3 casas decimais


if __name__ == '__main__':
    print("Autores: Aline Rocha de Jesus, Arthur Carvalho Rotkis, Bianca Silva Oliveira")
    print("O objetivo deste projeto é demonstrar, por meio de um código Python, as ondas eletromagnéticas,\nque são ondas capazes de propagar no vácuo e de se formarem pela combinação entre os campos elétricos e magnéticos,\nque são responsáveis pela onda de rádio, micro-ondas, infravermelho, luz visível, raios ultravioletas, raio X e raios gama.\nAlém disso, as ondas eletromagnéticas são classificadas de acordo com a frequência, oscilação e comprimento de onda, que também são representados dentro do código.")
    
    app = Main()

