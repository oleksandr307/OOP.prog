class Rational:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            parts = numerator.split('/')
            if len(parts) == 2:
                numerator = int(parts[0])
                denominator = int(parts[1])
            else:
                numerator = int(parts[0])
                denominator = 1

        if denominator == 0:
            raise ValueError("Denominator cannot be zero")


        def gcd(a, b):
            a, b = abs(a), abs(b)
            while b:
                a, b = b, a % b
            return a


        common_divisor = gcd(numerator, denominator)
        self.n = numerator // common_divisor
        self.d = denominator // common_divisor


        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Unsupported operand type for +")

        new_n = self.n * other.d + other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Unsupported operand type for -")

        new_n = self.n * other.d - other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Unsupported operand type for *")

        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Unsupported operand type for /")
        if other.n == 0:
            raise ZeroDivisionError("Division by zero")

        new_n = self.n * other.d
        new_d = self.d * other.n
        return Rational(new_n, new_d)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return Rational(other).__sub__(self)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return Rational(other).__truediv__(self)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Invalid key. Use 'n' or 'd'")

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Value must be integer")
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ValueError("Denominator cannot be zero")
            self.d = value
        else:
            raise KeyError("Invalid key. Use 'n' or 'd'")


        def gcd(a, b):
            a, b = abs(a), abs(b)
            while b:
                a, b = b, a % b
            return a


        common_divisor = gcd(self.n, self.d)
        self.n = self.n // common_divisor
        self.d = self.d // common_divisor


        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Rational({self.n}, {self.d})"


def evaluate_expression(expr):
    tokens = expr.split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ('*', '/'):
            left = Rational(tokens[i - 1])
            right = Rational(tokens[i + 1])
            if token == '*':
                res = left * right
            else:
                res = left / right
            tokens[i - 1:i + 2] = [str(res)]
            i -= 1
        i += 1


    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ('+', '-'):
            if i == 0:
                tokens[i:i + 2] = [str(-Rational(tokens[i + 1]))]
                continue
            left = Rational(tokens[i - 1])
            right = Rational(tokens[i + 1])
            if token == '+':
                res = left + right
            else:
                res = left - right
            tokens[i - 1:i + 2] = [str(res)]
            i -= 1
        i += 1

    return Rational(tokens[0])



def solve_equation():
    try:
        with open('input01.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        result = evaluate_expression(line)
                        print(f"{line} = {result}")
                    except Exception as e:
                        print(f"Error evaluating expression '{line}': {e}")
    except FileNotFoundError:
        print("File input01.txt not found")


if __name__ == "__main__":
    solve_equation()


