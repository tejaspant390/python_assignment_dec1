#Program to accepts the radius of a circle from the user and compute the area.

def area_of_circle(radius):
    pi = 22 / 7
    return pi * radius ** 2


radius = float(input('Enter the radius : '))
area = area_of_circle(radius)
print('The area of circle with radius {:.3f} is {:.3f}'.format(radius, area))