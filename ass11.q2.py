class animal:
    def animal_attribute(self):
        self.name="Tiger"
        self.speed="100Km/h"
        self.strangth="powerful"
        print("Name :{}\nSpeed :{}\nStrangth :{}".format(self.name,self.speed,self.strangth))

class tiger(animal):
    print("Nationl Animal")
    
a=animal()
b=tiger()
b.animal_attribute()
