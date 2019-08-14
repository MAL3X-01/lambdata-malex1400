class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self, addnum):
        return Complex(self.r + addnum.r,
                       self.i + addnum.i)

    def sub(self, subnum):
        return Complex(self.r - subnum.r,
                       self.i - subnum.i)


x = Complex(3.0, -4.5)
x.r, x.i
