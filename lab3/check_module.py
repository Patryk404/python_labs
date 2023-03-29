import zad2


circle = zad2.Circle(10)

print("Circle:")
print("Area: "+ str(circle.calc_area()))
print("Circuit: "+ str(circle.calc_circ() )+ "\n") 

square = zad2.Square(10)

print("Square: ")
print("Area: " + str(square.calc_area()))
print("Circuit: "+ str(square.calc_circ()) + "\n")

triangle = zad2.Triangle(10,10,10)

print("Triangle:")
print("Area: " + str(triangle.calc_area()))
print("Circuit: "+ str(triangle.calc_circ()) + "\n")  