print("Cop Details:")
class cop:
    def __init__(self):
        self.name="Aavi"
        self.age=21
        self.workexperience="8 year"
        self.designation="IPS"

    def add(self):
        print('Name: {}, Age: {}, WorkExperience: {},Desgnation:{}'.\
              format(self.name, self.age, self.workexperience,self.designation))

    
    def display(self):
        return(cop.add(self))
       
    def update(self,name,age,year,designation):
        print("New Officer:")
        self.name=name
        self.age=age
        self.workexperience=year
        self.designation=designation
        print('Name: {}, Age: {}, WorkExperience: {},Desgnation:{}'.\
              format(self.name, self.age, self.workexperience,self.designation))

class Mission(cop):
    def add_mission_details(self):
        print("Mission:")
        self.case="Kidnap"
        self.place="Delhi"
        print("Case:{} ,Place:{}".format(self.case,self.place))
        
    def available_Officer(self):
        print("Available Officer:")
        super().add()
    

     
d = cop()

d.display()

d.update("Arpan",22,"9 year","DIG")

n=Mission()

n.add_mission_details()

n.available_Officer()
