class mobilephone:

    __battery = 100 
    def charge(self):
       self.__battery+=10
       print(f"charge phone {self.__battery}")
    def usephone(self):
       self.__battery-=10
       print(f"charge phone {self.__battery}")
    def cheakbettry(self):
        print(f"charge phone {self.__battery}")

acc=mobilephone()
acc.cheakbettry()
acc.usephone()
acc.charge()  



