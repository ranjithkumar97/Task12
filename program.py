def volume_square_pyramid():
    b = int(input("enter the base area"))  # user to enter the base area values
    h = int(input("enter the height"))  # user to enter the height values
    c = 0.5
    volumr_pyramid = c * b * h
    print(volumr_pyramid)

def equilateral_triangle():
    a = int(input("enter the area "))  # user enter the area
    area = sqrt(3) / 4(a *a)  # formula
    print(area)

def Frustums():
    pi = 3.14
    r1 = int(input("enter the first radius"))  # user enter the radius1 value
    r2 = int(input("enter the second radius"))  # user enter the radius2 value
    h = int(input("enter the height"))  # user to enter the height values
    curved_surface = pi * h(r1 + r2)
    print(curved_surface)


def Hemisphere():
    pi = 3.14
    r = int(input("enter the radius"))  # user enter the radius value
    Curved_area = 2 * pi(r * r)  # formulas
    print(Curved_area)

def circle():
    pi = 3.14
    d = int(input("enter the diameter for the circle"))  # user will enter the diameter value
    area_circle = ((pi * d * d) / 4)  # formulas
    print(area_circle)
ch=int(input("enter your options fromm the used formulas"))

if ch==1:
  volume_square_pyramid()
elif ch==2:
  equilateral_triangle()
elif ch==3:
  Frustums()
elif ch==4:
  Hemisphere()
elif ch==5:
  circle()
else:
  print("wrong choice")
