class Point:  #ten freak musi byz z duzej litery
    def __init__(self, x, y): # magiczna funkcja, konstruktor klasy / prekazujemy x y do konstuktora
        self.x = x
        self.y = y
        self.default_color = "red"
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point.default_color)
point.z = 10 #przykladowa wartosc
print(point.x)
print(type(point))
print(isinstance(point, Point)) #point  jest instancja klasy Point
print(isinstance(point, int)) #point nie jest instancja obiektu klasy INT
point.draw()

another = Point(3,4)
print(another.default_color)
another.draw()