from abc import ABC
class vicale:
    def stop(self):
        pass
    def start(self):
        pass 

class car(vicale):
    def start(self):
        print("car started")

        

class bick(vicale):
    def start(self):
        print("bick started")

