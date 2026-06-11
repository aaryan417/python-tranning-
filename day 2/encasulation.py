class socail:
    __password ="aaryqn@123"
    __piture ="aaryan"
    __follwers =5000000

    def change_password(self, old, new):
      if old == self.__password:
        self.__password = new
        print("suuccefully change")

      else:
        print("worge pass")


    def add_folywers(self):
      self.__follwers +=1
      print(f"add folwers succesfuukly : {self.__follwers} ")


acc=socail()
acc.change_password("aaryqn@123","rahul@123" )

acc.add_folywers()

