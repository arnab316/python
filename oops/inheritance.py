class Car:
     def __init__(self, type):
      self.type = type
     @staticmethod
     def start():
      print("Starting")
     @staticmethod
     def stop():
      print("Stopping")

class ToyotaCar(Car):
       def __init__(self, name, type):
          super().__init__(type)
          self.name = name

car1 = ToyotaCar("fortuner", "Electric")
print(car1.name)
car1.start()
# print(car1.type)
