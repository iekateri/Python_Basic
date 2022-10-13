print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))
x_diff = x1 - x2
y_diff = y1 - y2
print("Уравнение прямой, проходящей через эти точки:")
if x2 - x1 != 0:
    k = y_diff / x_diff
    b = y2 - (k * x2)
    print(f"y = {k}x + {b}")
elif y1 == y2:
    b = y2
    print(f"y = {b}")
elif x1 == x2:
    print(f"x = {x1}")
else:
    print("Уравнение вида y = k * x + b составить нельзя")
