area_square=lambda side: side*side
area_rectangle=lambda length,breadth: length*breadth
area_triangle=lambda base,height: 0.5*base*height
s=float(input("Square side:"))
print("Area of square:",area_square(s))
length=float(input("rectangle length:"))
breadth=float(input("rectangle breadth:"))
print("Area of rectangle:",area_rectangle(length,breadth))
breadth=float(input("triangle base:"))
height=float(input("triangle height:"))
print("area of triangle:",area_triangle(breadth,height))
