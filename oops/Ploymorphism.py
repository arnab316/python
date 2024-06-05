class Complex:
    def __init__(self, number, img):
        self.number = number,
        self.img = img
    def showNumber(self):
         print(self.number , "i +" , self.img ,"j")

c1 = Complex(1,3)
c1.showNumber()