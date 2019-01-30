from math import *
def square():  #defnition for the area of square
    length=int(input("Enter the length")) #user to enter
    area_of_square=length*length #using formula
    print(area_of_square) #print the values
square() #by calling this function it will compile the output

def perimeter():#definition for Perimeter of a square
    length = int(input("Enter the length"))  # user to enter
    p=4*length #Perimeter of a square
    print(p)
perimeter()#by calling this function it will compile the output

def parallelogram(): #Definition for area of a parallelogram
    length=int(input("enter the first number for length")) #user to enter
    height=int(input("enter the second number for height")) #user to enter
    print(parallelogram)
parallelogram() #by calling this function it will compile the output

def Perimeter_parallelogram():
    length = int(input("enter the first number for length"))  # user to enter
    breath=int(input("enter the second number for breath")) #user to enter
    Perimeter_for_parralelgoram=2*(length+breath)
    print(Perimeter_for_parralelgoram)
Perimeter_parallelogram() #by calling this function it will compile the output

def triangle(): #defnition using triangle
    b=int(input("enter the base"))
    h=int(input("enter the height"))
    f=lambda b,h: b*h/2 #using anonoymous functions
    print(f)
triangle() #by calling this function it will compile the output

def isosceles_traingle():
    a=int(input("enter the two equal sides")) #user enter the two equal sides
    b=int(input("enter the base of isosceles triangle"))  #user to enter the two equal sides
    area_of_isosceles=(b/4)**(sqrt(4(a**2)-(b**2))) #b/4 exponent using square root _\frac{b}{4}sqrt{4a^2 - b^2}
    print(area_of_isosceles) #print the result
isosceles_traingle() #by calling this function it will compile the output

def trapezium():
    a=int(input("enter the first parallel sides")) #user enter the parallel side
    b=int(input("enyter the second parallel sides")) #user enter the parallel side
    h=int(input("enter the height")) #user enter the height
    area_of_trapezium=1/2**((a+b)*h) #using exponent
    print(area_of_trapezium)  #print the result
trapezium() #by calling this function it will compile the output

def diagonal_of_cuboid():
    l=int(input("enter the length")) #user enter the length
    b=int(input("enter the breath")) #user to enter the breath
    h=int(input("enter the height")) #user to enter the height
    area_of_diagonal=sqrt((l**2)(b**2)(h**2))
    print(area_of_diagonal)  #print the result
diagonal_of_cuboid()  #by calling this function it will compile the output

def cone():
    pi=3.14  #user enter the pi values
    r=int(input("enter the radius"))  #user enter the radius
    l-int(input("enter the length"))  #user enter the length
    area_of_cone=pi*r(r+l)
    print(area_of_cone)  #print the result
cone() #by calling this function it will compile the output

def right_circular_cone():
    pi=3.14
    r = int(input("enter the radius"))  # user enter the radius
    h = int(input("enter the height"))  # user to enter the height
    circular_cone=1/3*pi*r**2*h
    print(circular_cone)  #print the result
right_circular_cone() #by calling this function it will compile the output

def cylinder():
    pi=3.14
    r = int(input("enter the radius"))  # user enter the radius
    h = int(input("enter the height"))  # user to enter the height
    area_of_cylinder=2*pi*r(r+h)
    print(area_of_cylinder) #print the result
cylinder() #by calling this function it will compile the output

def surface_square_pyramid():
    a=int(input("enter the first input")) #user to enter the value of a
    b=int(input("enter the second input")) #user to enter the value of b
    area_of_surface=a*sqrt(4*b**2-a**2)
    print(area_of_surface)
surface_square_pyramid() #by calling this function it will compile the output

def volume_square_pyramid():
    b=int(input("enter the base area")) #user to enter the base area values
    h=int(input("enter the height")) #user to enter the height values
    volumr_pyramid=1/2*b*h
    print(volumr_pyramid)
volume_square_pyramid() #by calling this function it will compile the output

def  equilateral_triangle():
    a=int(input("enter the area ")) #user enter the area
    area=sqrt(3)/4(a**2) #formula
    print(area)
equilateral_triangle() #by calling this function it will compile the output

def  Frustums():
    pi=3.14
    r1=int(input("enter the first radius")) #user enter the radius1 value
    r2=int(input("enter the second radius")) #user enter the radius2 value
    h = int(input("enter the height"))  # user to enter the height values
    curved_surface=pi*h(r1+r2)
    print(curved_surface)
Frustums() #by calling this function it will compile the output

def Hemisphere():
    pi=3.14
    r=int(input("enter the radius")) #user enter the radius value
    Curved_area=2*pi(r**2)  #formulas
    print(Curved_area)
Hemisphere() #by calling this function it will compile the output

def circle():
    pi=3.14
    d=int(input("enter the diameter for the circle")) #user will enter the diameter value
    area_circle=((pi*d**2)/4) #formulas
    print(area_circle)
circle() #by calling this function it will compile the output







