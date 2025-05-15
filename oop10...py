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

    def __lt__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return (self.d, -self.n) < (other.d, -other.n)

    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Rational({self.n}, {self.d})"


class RationalList:
    def __init__(self, data=None):
        self.data = []
        if data is not None:
            for item in data:
                self.append(item)

    def append(self, item):
        if isinstance(item, (int, str)):
            item = Rational(item)
        if not isinstance(item, Rational):
            raise TypeError("Only Rational, int or str in format 'n/d' are allowed")
        self.data.append(item)

    def __iter__(self):
        sorted_data = sorted(self.data, reverse=True)
        return iter(sorted_data)

    def __str__(self):
        return str([str(item) for item in self.data])

    def sum(self):
        total = Rational(0)
        for num in self.data:
            total += num
        return total


def process_files():
    for filename in ['input01.txt', 'input02.txt', 'input03.txt']:
        try:
            with open(filename, 'r') as file:
                rational_list = RationalList()
                for line in file:
                    line = line.strip()
                    if line:
                        for token in line.split():
                            try:
                                rational_list.append(token)
                            except ValueError as e:
                                print(f"Invalid number format '{token}' in {filename}: {e}")

                print(f"\nFile: {filename}")
                print("Original order:", rational_list)
                print("Sorted (descending denominators, then numerators):")
                for rational in rational_list:
                    print(rational)
                print("Sum:", rational_list.sum())

        except FileNotFoundError:
            print(f"\nFile {filename} not found")
        except Exception as e:
            print(f"\nError processing {filename}: {e}")


if __name__ == "__main__":
    process_files()