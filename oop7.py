class Figure:
    def dim(self):
        raise NotImplementedError("метод не реалізовано")
    def perimetr(self):
        return None
    def area(self):
        return None
    def area_surfase(self):
        return None
    def area_base(self):
        return None
    def volume(self):
        raise NotImplementedError("метод не реалізовано")


class Triangle(Figure):
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
    def dim(self):
        return 2
    def volume(self):
        return None
    def area_base(self):
        return None
    def area_surfase(self):
        return None

if __name__ =='__main__':
    t1 = Triangle(23, 21, 20)
    print(t1.perimetr())
    print(t1.area())
    print(t1.area_base())
    print(t1.area_surfase())
    print(t1.dim())
    print(t1.volume())



class Rectangle(Figure):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def perimetr(self):
        return 2*self.a + 2*self.b
    def area(self):
        return self.a*self.b
    def dim(self):
        return 2
    def volume(self):
        return None
    def area_surfase(self):
        return None
    def area_base(self):
        return None


if __name__ == '__main__':
    r1 = Rectangle(22, 5)
    print(r1.perimetr())
    print(r1.area())
    print(r1.area_base())
    print(r1.area_surfase())
    print(r1.dim())
    print(r1.volume())

class Circle(Figure):
    def __init__(self, r):
        self.r=r
    def perimetr(self):
        return 2*3.14*self.r
    def area(self):
        return 3.14*self.r**2
    def dim(self):
        return 2
    def volume(self):
        return None
    def area_base(self):
        return None
    def area_surfase(self):
        return None

if __name__ == '__main__':
    c1 = Circle(0)
    print(c1.perimetr())
    print(c1.area())
    print(c1.area_base())
    print(c1.area_surfase())
    print(c1.dim())
    print(c1.volume())


class Paralelogram(Figure):
    def __init__(self, a, b, h):
        self.a=a
        self.b=b
        self.h=h
    def perimetr(self):
        return 2*self.a + 2*self.b
    def area(self):
        return self.a*self.h
    def dim(self):
        return 2
    def volume(self):
        return None
    def area_base(self):
        return None
    def area_surfase(self):
        return None

if __name__ == '__main__':
    p1 = Paralelogram(1, 16, 6)
    print(p1.perimetr())
    print(p1.area())
    print(p1.area_base())
    print(p1.area_surfase())
    print(p1.dim())
    print(p1.volume())



class Trapeze(Figure):
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
    def dim(self):
        return 2
    def volume(self):
        return None
    def area_base(self):
        return None
    def area_surfase(self):
        return None

if __name__ =='__main__':
    tr1 = Trapeze(20, 6 ,23 ,3 ,9 )
    print(tr1.perimetr())
    print(tr1.area())
    print(tr1.area_base())
    print(tr1.area_surfase())
    print(tr1.dim())
    print(tr1.volume())


class Triangle_pyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h=h
    def perimetr(self):
        return None
    def area(self):
        return None
    def area_surfase(self):
        p1 = self.a/2 + self.h
        s1 = (p1-self.a)*(p1-self.a)*(p1-self.h)
        return 3*(s1**0.5) + (self.a**2)*(3**0.5)/4
    def area_base(self):
        return (self.a**2)*(3**0.5)/4
    def volume(self):
        return (self.a**2)*(3**0.5)/4*self.h/3
    def dim(self):
        return 3
if __name__=='__main__':
    trp1 = Triangle_pyramid(21,10)
    print(trp1.perimetr())
    print(trp1.area())
    print(trp1.area_base())
    print(trp1.area_surfase())
    print(trp1.dim())
    print(trp1.volume())


class Rectangle_pyramyd(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h=h
    def perimetr(self):
        return None
    def area(self):
        return None
    def area_surfase(self):
        p1 = self.a/2 + self.h
        s1 = p1 * (p1 - self.a) * (p1 - self.a) * (p1 - self.h)
        p2 =self.b/2 + self.h
        s2 =  p2* (p2 - self.b) * (p2 - self.b) * (p2 - self.h)
        return self.a*self.b + 2*s1**0.5 + 2*s2**0.5
    def area_base(self):
        return self.a*self.b
    def volume(self):
        return self.a*self.b*self.h/3
    def dim(self):
        return 3

if __name__=='__main__':
    rp1 = Rectangle_pyramyd(14, 18, 22)
    print(rp1.perimetr())
    print(rp1.area())
    print(rp1.area_base())
    print(rp1.area_surfase())
    print(rp1.dim())
    print(rp1.volume())





class Box(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
    def dimention(self):
        return 3
    def area_base(self):
        return self.a * self.b
    def area_surfase(self):
        return 2 * (self.a * self.b + self.a * self.h + self.b * self.h)
    def volume(self):
        return self.a * self.b * self.h
    def perimetr(self):
        return None
    def area(self):
        return None

if __name__ == '__main__':
    b1 = Box(9, 16, 5)
    print(b1.perimetr())
    print(b1.area())
    print(b1.area_base())
    print(b1.area_surfase())
    print(b1.dim())
    print(b1.volume())




class Ball:
    def __init__(self, r):
        self.r=r
    def dim(self):
        return 3
    def perimetr(self):
        return None
    def area(self):
        return None
    def area_surfase(self):
        return 4*3.14*self.r
    def area_base(self):
        return 3.14*self.r**2
    def volume(self):
        return 3/4*3.14*self.r**3

if __name__ == '__main__':
    ba1 = Ball(24)
    print(ba1.perimetr())
    print(ba1.area())
    print(ba1.area_base())
    print(ba1.area_surfase())
    print(ba1.dim())
    print(ba1.volume())




class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h=h
    def dim(self):
        return 3
    def perimetr(self):
        return None
    def area(self):
        return None
    def area_base(self):
        return 3.14*self.r**2
    def area_surfase(self):
        l = (self.r**2 + self.h**2)**0.5
        s = 3.14*self.r*l
        return s
    def volume(self):
        return (3.14*self.r**2)*self.h/3


if __name__ =='__main__':
    co1 = Cone(20, 2)
    print(co1.perimetr())
    print(co1.area())
    print(co1.area_base())
    print(co1.area_surfase())
    print(co1.dim())
    print(co1.volume())



class Triangle_pryzma(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b ,c)
        self.h = h
    def dim(self):
        return 3
    def perimetr(self):
        return None
    def area(self):
        return None
    def area_base(self):
        p = (self.a + self.b + self.c) / 2
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        return s**0.5
    def area_surface(self):
        p = (self.a + self.b + self.c) / 2
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        return self.a*self.h + self.b*self.h * self.c*self.h + 2*(s**0.5)
    def volume(self):
        p = (self.a + self.b + self.c) / 2
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        return (s**0.5)*self.h

if __name__ =='__main__':
    trpr1 = Triangle_pryzma(14, 8, 4, 23)
    print(trpr1.perimetr())
    print(trpr1.area())
    print(trpr1.area_base())
    print(trpr1.area_surfase())
    print(trpr1.dim())
    print(trpr1.volume())




figures = [Triangle_pryzma(14, 8, 4, 23),Cone(20, 2), Ball(24), Box(9, 16, 5),
 Rectangle_pyramyd(14, 18, 22), Triangle_pyramid(21,10), Trapeze(20, 6 ,23 ,3 ,9 ),
           Paralelogram(1, 16, 6), Circle(0), Rectangle(22, 5), Triangle(23, 21, 20)  ]



def max_volume(figures):
    max_figure_vol = None
    max_value = float

    for fig in figures:
        v = fig.volume()
        if v is not None and v > max_value:
            max_value = v
            max_figure_vol = fig

    return max_figure_vol

def max_area(figures):
    max_figure_ar = None
    max_value = float

    for fig in figures:
        a = fig.area()
        if a is not None and a > max_value:
            max_value = a
            max_figure_ar = fig

    return max_figure_ar

def max_area_base(figures):
    max_figure_ar_base = None
    max_value = float

    for fig in figures:
        ab = fig.area_base()
        if ab is not None and ab > max_value:
            max_value = ab
            max_figure_ar_base = fig

    return max_figure_ar_base

def max_area_surfase(figures):
    max_figure_ar_surfase = None
    max_value = float

    for fig in figures:
        a_s = fig.area_surfase()
        if a_s is not None and a_s > max_value:
            max_value = a_s
            max_figure_ar_surfase = fig

    return max_figure_ar_surfase
def max_perimetr(figures):
    max_figure_per = None
    max_value = float

    for fig in figures:
        p = fig.perimetr()
        if p is not None and p > max_value:
            max_value = p
            max_figure_per = fig

    return max_figure_per














































