import math

class Complex(object):
    
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        x=self.real+no.real
        y=self.imaginary+no.imaginary
        return Complex(x,y)

    def __sub__(self, no):
        x=self.real-no.real
        y=self.imaginary-no.imaginary
        return Complex(x,y)
    
    def __mul__(self, no):
        x=self.real*no.real-self.imaginary*no.imaginary
        y=self.real*no.imaginary+self.imaginary*no.real
        return Complex(x,y)
        # pass
    
    def __div__(self, no):
        sq_add=(no.real**2)+(no.imaginary**2)
        x=((self.real*no.real)+(self.imaginary*no.imaginary))/sq_add
        y=((self.imaginary*no.real)-(self.real*no.imaginary))/sq_add
        return Complex(x,y)
        
    def mod(self):
        return Complex(pow((self.real**2+self.imaginary**2),0.5),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':