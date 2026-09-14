"""
CLASS
1) What is class
2) Ordinary vs static properties
3) Special methods
"""

print("=======What is class==========")

class Person():

    #state
    message='class state property'

    #constructor
    def __init__(self,name, age):
        self.name = name
        self.age = age

    #method
    def introduce(self):
        print(self.name, "says: Salom")

    def say_age(self):
        print(self.name, "is", self.age, "year old" )

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 =Person('Justin', 25)
person2 =Person("Tyler", 20)
person3 =Person("Martin", 30)


person1.introduce()
person2.say_age()




print("======ordinary vs static property==============")

new= Person.message
print(new)

Person.explain()
#static method



print("===============special methods==============")



#Pythons most common special methods:
#__init__, __new__, __str__, __call__,__eg__,__len__

class Car():
    #state
    description="this class makes cars"

    #constructor
    def __new__(cls,*args):
        print("__new__")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name= name
        self.year =year

    #method
    def start_engine(self):
        print(self.name, "started!!!")

    def stop_engine(self):
        print(self.name, "stopped!!!")

    def __str__(self):
        return f"{self.name} mashinasi {self.year} da ishlab chiqarilgan"

    def __call__(self):
        print("bu fucntion kabi chaqrildi!!!")
        return True
    


    
mycar= Car("Spark", 2025)
mycar.start_engine()
mycar.stop_engine()

your_car= Car("toyot", 2000)
print(your_car)
your_car() #fucntion kabi

res= your_car()
print(res)



