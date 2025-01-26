"""Complex class that introduces operator overloading"""
class ComplexOperator:
    def __init__(self, real, imaginary):
        #initializing the instance of class
        self.real = real
        self.imaginary = imaginary
    #overload the + operator
    def __add__(self, other):
        return ComplexOperator(self.real + other.real, self.imaginary + other.imaginary)
    #overload the - operator
    def __sub__(self, other):
        return ComplexOperator(self.real - other.real, self.imaginary - other.imaginary)
    #overload the multiplication operator
    def __mul__(self, other):
        return ComplexOperator(self.real * other.real, self.imaginary * other.imaginary)
    #overload the division operator
    def __truediv__(self, other):
        return complex(self.real / other.real, self.imaginary / other.imaginary)
    #overloads the plus equal operator
    def  __iadd__(self, other):
        self.real += other.real
        self.imaginary += other.imaginary
        return self
    #overlaods -= operators
    def __isub__(self, other):
        self.real -= other.real
        self.imaginary -= other.imaginary
        return self
    def __repr__(self):
        ":returns: String representation of complex number"
        return (f"{self.real}" +
                (" +" if self.imaginary > 0 else " -" )+
                f" {abs(self.imaginary)}i")
    #class the class
x = ComplexOperator(real= 2, imaginary=3)
print(x)
y =ComplexOperator(real= 5, imaginary=-2)
print(y)
print(x + y)
print(x - y)
x += y
print(x)


