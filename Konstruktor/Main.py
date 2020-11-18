class Hero: #templete
    jumlah = 0
    #Konstruktor
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat nama dengan " + inputName)

    #Desktruktor
    def __del__(self):
        class_name = self.__class__.__name__
        Hero.jumlah -= 1
        print("sebuah objek",class_name,",yaitu", self.name,"dihapus")

#instansiasi
print(Hero.jumlah)       
hero1 = Hero("sniper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup", 1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

#delete
del hero2
print("Jumlah Hero :" ,Hero.jumlah)