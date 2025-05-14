import math


class Figure:
    def dimension(self):
        raise NotImplementedError("Метод dimension() не реалізовано")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() не реалізовано")

    def square(self):
        raise NotImplementedError("Метод square() не реалізовано")

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        raise NotImplementedError("Метод volume() не реалізовано")



class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def volume(self):
        return self.square()


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    def dimension(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        return ((self.a + self.b) / 2) * math.sqrt(
            self.c ** 2 - (((self.b - self.a) ** 2 + self.c ** 2 - self.d ** 2) / (2 * (self.b - self.a))) ** 2
        )

    def volume(self):
        return self.square()


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = float(a)
        self.b = float(b)
        self.h = float(h)

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()


class Circle(Figure):
    def __init__(self, r):
        self.r = float(r)

    def dimension(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    def volume(self):
        return self.square()



class Ball(Figure):
    def __init__(self, r):
        self.r = float(r)

    def dimension(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * self.r ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.r ** 3


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h_pyramid = float(h)

    def dimension(self):
        return 3

    def squareSurface(self):
        apothem = math.sqrt((self.a / (2 * math.sqrt(3))) ** 2 + self.h_pyramid ** 2)
        return 3 * (0.5 * self.a * apothem)

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h_pyramid

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h_pyramid


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h_pyramid = float(h)

    def dimension(self):
        return 3

    def squareSurface(self):
        apothem_a = math.sqrt((self.b / 2) ** 2 + self.h_pyramid ** 2)
        apothem_b = math.sqrt((self.a / 2) ** 2 + self.h_pyramid ** 2)
        return self.a * apothem_a + self.b * apothem_b

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h_pyramid

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h_pyramid


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = float(c)

    def dimension(self):
        return 3

    def squareSurface(self):
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)

    def height(self):
        return self.c

    def volume(self):
        return self.a * self.b * self.c


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = float(h)

    def dimension(self):
        return 3

    def squareSurface(self):
        l = math.sqrt(self.r ** 2 + self.h ** 2)
        return math.pi * self.r * l

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h_prism = float(h)

    def dimension(self):
        return 3

    def squareSurface(self):
        return self.perimeter() * self.h_prism + 2 * super().square()

    def height(self):
        return self.h_prism

    def volume(self):
        return super().square() * self.h_prism


def create_figure_from_line(line):
    parts = line.strip().split()
    if not parts:
        return None

    fig_type = parts[0]
    params = parts[1:]

    try:
        if fig_type == "Triangle":
            return Triangle(*params)
        elif fig_type == "Rectangle":
            return Rectangle(*params)
        elif fig_type == "Trapeze":
            return Trapeze(*params)
        elif fig_type == "Parallelogram":
            return Parallelogram(*params)
        elif fig_type == "Circle":
            return Circle(*params)
        elif fig_type == "Ball":
            return Ball(*params)
        elif fig_type == "TriangularPyramid":
            return TriangularPyramid(*params)
        elif fig_type == "QuadrangularPyramid":
            return QuadrangularPyramid(*params)
        elif fig_type == "RectangularParallelepiped":
            return RectangularParallelepiped(*params)
        elif fig_type == "Cone":
            return Cone(*params)
        elif fig_type == "TriangularPrism":
            return TriangularPrism(*params)
        else:
            return None
    except:
        return None


def find_figure_with_max_volume(file_path):
    max_figure = None
    max_volume = -1

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                figure = create_figure_from_line(line)
                if figure:
                    try:
                        current_volume = figure.volume()
                        if current_volume is not None and current_volume > max_volume:
                            max_volume = current_volume
                            max_figure = figure
                    except:
                        continue
    except:
        return None, None

    return max_figure, max_volume


def process_files(input_files, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.write("Результати аналізу фігур:\n\n")

            for file in input_files:
                try:
                    figure, volume = find_figure_with_max_volume(file)
                    out_f.write(f"Файл: {file}\n")

                    if figure:
                        out_f.write(f"Фігура з найбільшою мірою: {figure.__class__.__name__}\n")
                        out_f.write(f"Міра: {volume:.2f}\n\n")
                    else:
                        out_f.write("Не знайдено валідних фігур\n\n")

                except Exception as e:
                    out_f.write(f"Помилка при обробці файлу {file}: {str(e)}\n\n")

        print(f"Файл {output_file} успішно створено за шляхом: {os.path.abspath(output_file)}")
        return True

    except Exception as e:
        print(f"Помилка при створенні файлу: {str(e)}")
        return False


if __name__ == "__main__":

    files = ["input01.txt", "input02.txt", "input03.txt"]

    for file in files:
        print(f"\nОбробка файлу {file}:")
        figure, volume = find_figure_with_max_volume(file)

        if figure:
            print(f"Фігура з найбільшою мірою: {figure.__class__.__name__}")
            print(f"Міра: {volume:.2f}")
        else:
            print("Не знайдено жодної валідної фігури або файл не існує")

output_file = r"C:\Users\sokol\OOP.prog\output.txt"

