from abc import ABC,abstractmethod


class ATM(ABC):
    @abstractmethod
    def withdrall(self):
        pass
    @abstractmethod
    def cheakbal(self):
        pass



class sbi(ATM):
    def withdrall(self):
        server ="dxc sxscsvxcvv "

        print(f"ash withdrall ")


    def cheakbal (self):
        server ="wqewsddffsdcvccsdvb"
        print("bal = 2345")

a= sbi()
a.withdrall()
a.cheakbal()        


          
        