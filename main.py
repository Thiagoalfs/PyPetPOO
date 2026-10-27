class Pet:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.fome = 50
        self.felicidade = 50
        self.energia = 50
    def alimentar(self):
        self.fome -= 10
        self.felicidade += 5
        self.fome = max(self.fome, 0)
        self.felicidade = min(self.felicidade, 100)
        print(f"{self.nome} comeu!")
    def brincar(self):
        if self.energia <= 0:
            print(f"{self.nome} está cansado demais!")
            return
        self.felicidade += 10
        self.energia -= 10
        self.fome += 10
        self.felicidade = min(self.felicidade, 100)
        self.energia = max(self.energia, 0)
        self.fome = min(self.fome, 100)
        print(f"{self.nome} brincou!")
    def dormir(self):
        self.energia += 30
        self.fome += 5
        self.energia = min(self.energia, 100)
        self.fome = min(self.fome, 100)
        print(f"{self.nome} dormiu!")
    def verificar_estado(self):
        if self.fome >= 100:
            print(f"{self.nome} morreu de fome!")
            return False
        if self.felicidade <= 0:
            print(f"{self.nome} morreu de tristeza!")
            return False
        if self.energia <= 0:
            print(f"{self.nome} morreu de cansaço!")
            return False
        return True
    def mostrar_status(self):
        print("STATUS")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Fome: {self.fome}/100")
        print(f"Felicidade: {self.felicidade}/100")
        print(f"Energia: {self.energia}/100")

pet = Pet("Bilu", "Gato")

while True:
    print("=" * 30)
    print("PET VIRTUAL - PyPet!")
    print("=" * 30)
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Dormir")
    print("4 - Ver status")
    print("5 - Sair")
    opcao = input("\nEscolha uma opção: ")
    if opcao == "1":
        pet.alimentar()
    elif opcao == "2":
        pet.brincar()
    elif opcao == "3":
        pet.dormir()
    elif opcao == "4":
        pet.mostrar_status()
    elif opcao == "5":
        print("Até a próxima!")
        break
    if not pet.verificar_estado():
        print("O Pet morreu :/")
        break