import math
print('Successfully imported geometry.py')

def circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

def tri_hypotenuse(leg, base):
    hypotenuse = math.sqrt((int(leg) ** 2) + (int(base) ** 2))
    print(hypotenuse)

leg = input('Leg: ')
base = input('Base: ')
tri_hypotenuse(leg, base)

