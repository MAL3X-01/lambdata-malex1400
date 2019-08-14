class Complex:
    """
    Class object to represent complex numbers.

    PARAMETERS
    ==========
    realpart: real part of the complex number
    imagpart: imaginary part of the complex number
    """
    def __init__(self, realpart, imagpart):
        " Initializing the class object "
        self.r = realpart
        self.i = imagpart

    def add(self, addnum):
        " Adding a complex number to the class "
        return Complex(self.r + addnum.r,
                       self.i + addnum.i)

    def sub(self, subnum):
        " subtracting a complex number from the class "
        return Complex(self.r - subnum.r,
                       self.i - subnum.i)

# sanity checks.
x = Complex(3.0, -4.5)
x.r, x.i
