import math
import os


class Complex:
    def __init__(self, real, i):
        self.real = real
        self.i = i

    def getReal(self):
        return self.real

    def getI(self):
        return self.i

    def setReal(self, r):
        self.real = r

    def setI(self, i):
        self.i = i
    
    def add(self, z2):
        z3 = Complex(0.0, 0.0)
        z3.setReal(self.getReal() + z2.getReal())
        z3.setI(self.getI() + z2.getI())
        self.setReal(z3.getReal())
        self.setI(z3.getI())

    def multiply(self, z2):
        z3 = Complex(0.0, 0.0)
        z3.setReal((self.getReal() * z2.getReal()) - (self.getI() * z2.getI()))
        z3.setI((self.getReal() * z2.getI()) + (self.getI() * z2.getReal()))
        self.setReal(z3.getReal())
        self.setI(z3.getI())

    def getAV(self):
        return math.sqrt(self.getReal() * self.getReal() + self.getI() * self.getI())

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def getR(self):
        return self.r
    
    def getG(self):
        return self.g
    
    def getB(self):
        return self.b

    def setColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Pixel:
    def __init__(self, z, color):
        self.z = z
        self.color = color

    def getComplex(self):
        return self.z

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
    
    def setComplex(self, z):
        self.z = z

def getReal(i):
    ratio = (scale * 2.0) / float(resolution)
    return ((i - (resolution / 2)) * ratio)  + point.getReal()

def getComplex(i):
    ratio = (scale* 2.0) / float(resolution)
    return (-1 * (i - (resolution / 2.0)) * ratio)  + point.getI()

def caculateColor(i):
    hue = i % 192
    color = Color(0, 0, 0)
    if(hue < 192):
        color.setColor(256, (256 - (hue - 160) * 8), 0)
        return color
    if(hue < 160):
        color.setColor(((hue - 128) * 8), 256, 0)
        return color
    if(hue < 128):
        color.setColor(0, 256, (256 - (hue - 96) * 8))
        return color
    if(hue < 96):
        color.setColor(0, ((hue - 64) * 8), 256)
        return color
    if(hue < 64):
        color.setColor((256 - (hue - 32) * 8), 0, 256)
        return color
    if(hue < 32):
        color.setColor(0, 0, (hue * 8))
        return color
    
    

def computeMandebrot(screen):
    for x in screen:
        z = Complex(0.0, 0.0)
        i = 0
        c = x.getComplex()
        while( (z.getAV() < 2) and (i < maxDepth)):
            z.multiply(z)
            z.add(c)
            i += 1
        if(i >= maxDepth):
            #color = Color(0, 0, 0)
            #x.setColor(color)
            x.setColor(0)
        else:
            #x.setColor(caculateColor(i))
            x.setColor(1)

def generate():
    for i in range(resolution * resolution):
        #color = Color(0, 0, 0)
        color = 0
        complex = Complex(getReal(i % resolution), getComplex(int(i / resolution)))
        pixel = Pixel(complex, color)
        screen.append(pixel)
    
    computeMandebrot(screen)
    display(screen)
    
def display(screen):
    f = open("mandelbrot.txt", "w")
    f.write("")
    f.close()
    f = open("mandelbrot.txt", "a")
    i = 1
    line = ""
    for x in screen:
        if(x.getColor() == 1):
            line += "_"
        else:
            line += "#"
        if (((i + 1) % resolution) == 0):
            line += "\n"
            f.write(line)
            line = ""
        i += 1
    f.close()
        

screen = []
print("center point\n Real")
r = float(input())
print("complex")
i = float(input())
point = Complex(r, i)
print("image scale")
scale = float(input())
print("image size")
resolution = int(input())
print("detale level")
maxDepth = int(input())

generate()

