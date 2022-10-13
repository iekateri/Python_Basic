import math

print("Введите координаты монетки: ")
x_point = float(input("X: "))
y_point = float(input("Y: "))
r_circle = float(input("Введите радиус: "))

hypotenuse = math.sqrt(x_point ** 2 + y_point ** 2)

if hypotenuse <= r_circle:
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")
