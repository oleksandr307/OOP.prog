PI = 3.14


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        value = s * (s - self.a) * (s - self.b) * (s - self.c)
        if value <= 0:
            return 0
        return value ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        h = 3
        return ((self.a + self.b) / 2) * h

    def perimeter(self):
        return self.a + self.b + self.c + self.d

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return self.a * self.h

    def perimeter(self):
        return 2 * (self.a + self.b)

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return PI * self.r * self.r

    def perimeter(self):
        return 2 * PI * self.r

def parse_shape(line):
    parts = line.strip().split()
    name = parts[0]
    params = list(map(float, parts[1:]))

    if name == "Triangle" and len(params) == 3:
        return Triangle(*params)
    elif name == "Rectangle" and len(params) == 2:
        return Rectangle(*params)
    elif name == "Trapeze" and len(params) == 4:
        return Trapeze(*params)
    elif name == "Parallelogram" and len(params) == 3:
        return Parallelogram(*params)
    elif name == "Circle" and len(params) == 1:
        return Circle(*params)
    else:
        return None

def main(input_file):
    shapes = []

    with open(input_file, 'r') as file:
        for line in file:
            shape = parse_shape(line)
            if shape:
                shapes.append(shape)

    if not shapes:
        print("Жодної валідної фігури не знайдено.")
        return

    max_area_shape = max(shapes, key=lambda s: s.area())
    max_perimeter_shape = max(shapes, key=lambda s: s.perimeter())

    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(f"Фігура з найбільшою площею: {type(max_area_shape).__name__}\n")
        out.write(f"Площа: {max_area_shape.area():.2f}\n")
        out.write(f"Фігура з найбільшим периметром: {type(max_perimeter_shape).__name__}\n")
        out.write(f"Периметр: {max_perimeter_shape.perimeter():.2f}\n")

if __name__ == "__main__":
    main("input01.txt")


