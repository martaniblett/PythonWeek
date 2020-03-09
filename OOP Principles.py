from abc import abstractmethod

#create superclass
class  Bird:
    fly = True
    
    def noise(self):
        print ("Birdnoise")
    
    babies = 0

    def reproduce(self):
        self.babies +=1
    
    @abstractmethod
    def eat(self):
        pass

    extinct = False

#create subclass 
class Owl(Bird):

    def reproduce (self):
        self.babies +=6

    def eat(self):
        print ("Peck Peck")

owl_1 = Owl()
owl_1.eat()



# add another subclass
class Dodo(Bird):
    Fly = False
    extinct = True

def eat(self):
    print ("Nom Nom")

def reproduce(self):
    if self.extinct == False:
        self.babies += 1
    else:
        print ("no more dodo's")

dodo1 = Dodo()
dodo1.reproduce()