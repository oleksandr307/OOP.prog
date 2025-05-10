class Triangle:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    def perimetr(self):
        return self.a + self.b + self.c
    def area(self):
        p = (self.a + self.b +self.c) / 2
        s = p*(p-self.a)*(p-self.b)*(p-self.c)
        return s**0.5
if __name__ =='__main__':
    t1 = Triangle(23, 21, 20)
    print(t1.perimetr())
    print(t1.area())

class Rectangle:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def perimetr(self):
        return 2*self.a + 2*self.b
    def area(self):
        return self.a*self.b
if __name__ == '__main__':
    r1 = Rectangle(22, 5)
    print(r1.perimetr())
    print(r1.area())

class Circle:
    def __init__(self, r):
        self.r=r
    def perimetr(self):
        return 2*3.14*self.r
    def area(self):
        return 3.14*self.r**2
if __name__ == '__main__':
    c1 = Circle(0)
    print(c1.perimetr())
    print(c1.area())

class Paralelogram:
    def __init__(self, a, b, h):
        self.a=a
        self.b=b
        self.h=h
    def perimetr(self):
        return 2*self.a + 2*self.b
    def area(self):
        return self.a*self.h
if __name__ == '__main__':
    p1 = Paralelogram(1, 16, 6)
    print(p1.perimetr())
    print(p1.area())    
class Trapeze:
    def __init__(self, a ,b, c, d, h):
        self.a=a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
    def perimetr(self):
        return self.a+ self.b +self.c + self.d
    def area(self):
        return (self.a + self.b)/2*self.h
if __name__ =='__main__':
    tr1 = Trapeze(20, 6, 23, 3, 9)
    print(tr1.perimetr())
    print(tr1.area())


figures = [
    Circle(0),
    Rectangle(22, 5),
    Triangle(23, 21, 20),
    Paralelogram(1, 16, 6),
    Trapeze(20, 6, 23, 3, 9),
    Circle(0),
    Rectangle(22, 5),
    Triangle(23, 21, 20),
    Paralelogram(1, 16, 6)
]


max_area_figure = figures[0]
max_perimetr_figure = figures[0]


for figure in figures[1:]:
    if figure.area() > max_area_figure.area():
        max_area_figure = figure
    if figure.perimetr() > max_perimetr_figure.perimetr():
        max_perimetr_figure = figure


print("Фігура з найбільшою площею:")
print(f"{max_area_figure} Площа = {max_area_figure.area():.2f}")

print("\Фігура з найбільшим периметром:")
print(f"{max_perimetr_figure} ->Периметр = {max_perimetr_figure.perimetr():.2f}")