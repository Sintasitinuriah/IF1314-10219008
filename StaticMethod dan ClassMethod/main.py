class Hero :
    # private class Variabel
    __jumlah = 0;

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1
    
    # method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk object tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    #method static (decorator) nempel ke object class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

sniper = Hero('sniper')
print(Hero.getJumlah3())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah3())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())