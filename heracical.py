class father:
    def home(self):
        print ("parrent home")


class son(father):
    def leving(self):
        print ("son leave in fathe home")


class doughter(father):
    def leving(self):
        print ("daughter leave in father home")        



s= doughter()
s2= son()
s2.home()
s2.leving() 
s.leving()       