def Xk(x, k):
    X0 = 1.0
    for i in range(1, k+1):
        X0 *= x**2 / ((2*i) * (2*i - 1))
    return X0

def Xk_generator(x):
    Xk = 1.0
    k = 1
    yield Xk
    while True:
        Xk *= x**2 / ((2*k) * (2*k - 1))
        yield Xk
        k += 1

def Pn(n):
    prod = 1.0
    for i in range(1, n+1):
        prod *= (1 + 1 / i**2)
    return prod

def Pn_generator():
    product = 1.0
    i = 1
    while True:
        product *= (1 + 1 / i**2)
        yield product
        i += 1


import math

def calculate_y(x, epsilon):
    if abs(x) >= 1:
        raise ValueError("|x| < 1")
    term = x
    total = term
    k = 1
    while True:
        term *= x**2
        next_term = term / (2*k + 1)
        if abs(next_term) < epsilon:
            break
        total += next_term
        k += 1
    return 2 * total

x = 0.5
epsilon = 1e-6
y_calculated = calculate_y(x, epsilon)
y_import_math = math.log((1 + x) / (1 - x))
print(f"Розраховане: {y_calculated}, Бібліотечне: {y_import_math}")



def calculate_Sn(n):
    A = [0, 1, 1, 1]  # a[1], a[2], a[3]
    sum = 0.0
    for k in range(1, n+1):
        if k <= 3:
            Ak = 1
        else:
            Ak = A[k-1] + A[k-3]
            A.append(Ak)
        sum += Ak / (2**k)
    return sum

