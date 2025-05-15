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

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if isinstance(value, (int, str)):
            value = Rational(value)
        if not isinstance(value, Rational):
            raise TypeError("Only Rational, int or str in format 'n/d' are allowed")
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        new_list = RationalList(self.data.copy())
        if isinstance(other, RationalList):
            new_list.data.extend(other.data)
        elif isinstance(other, (Rational, int, str)):
            new_list.append(other)
        else:
            raise TypeError("Unsupported operand type for +")
        return new_list

    def __radd__(self, other):
        new_list = RationalList()
        if isinstance(other, (Rational, int, str)):
            new_list.append(other)
        else:
            raise TypeError("Unsupported operand type for +")
        new_list.data.extend(self.data)
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.data.extend(other.data)
        elif isinstance(other, (Rational, int, str)):
            self.append(other)
        else:
            raise TypeError("Unsupported operand type for +=")
        return self

    def __str__(self):
        return str([str(item) for item in self.data])

    def sum(self):
        total = Rational(0)
        for num in self.data:
            total += num
        return total


def solve_eqution():
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

                print(f"File: {filename}")
                print(f"Numbers: {rational_list}")
                print(f"Sum: {rational_list.sum()}")
                print()

        except FileNotFoundError:
            print(f"File {filename} not found")
        except Exception as e:
            print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    solve_eqution()