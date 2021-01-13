class car:
    def __init__(self,model,brand,color):
        self.model=model
        self.brand=brand
        self.color=color
    def start(self):
        print("The car has started")
    def move(self):
        print("The car is moving")
    def stop(self):
        print("The car has been stop")
    

class bmw(car):
    def __init__(self,model,brand,color):
        super().__init__(model,brand,color)
    def info(self):
        print("Model:",self.model)
        print("Brand:",self.brand)
        print("Color:",self.color)
    def autostart(self):
        print("Tt has auto start feature")
    def autogear(self):
        print("It has auto gear feature")

print("OUTPUT")
car1=bmw(110,"BMW","Black")
car1.info()
car1.start()
car1.move()
car1.stop()
car1.autostart()
car1.autogear()
#OUTPUT
"""
python CarInheritance.py

OUTPUT
Model: 110
Brand: BMW
Color: Black
The car has started
The car is moving
The car has been stop
Tt has auto start feature
It has auto gear feature

"""
