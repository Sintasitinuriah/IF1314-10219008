class HandPhone:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} dengan Kecepatan {}".format(
            self.name,
            self.speed
            )
        )

class Hp_biasa(HandPhone):
    def __init__(self,name):
        super().__init__(name,100)
        
    # Override
    def showInfo(self):
        print("showinfo di subclass Hp_biasa")
        print("{} \n\t Tipe: Biasa, \n\tspeed : {}".format(
            self.name, 
            self.speed
            )
        )

class Hp_gaming(HandPhone):
    def __init__(self,name):
        super().__init__(name,500)
        super().showInfo()

asusROG = Hp_gaming('asusROG')
samsungA21 = Hp_biasa('samsungA21')

asusROG.showInfo()
samsungA21.showInfo()