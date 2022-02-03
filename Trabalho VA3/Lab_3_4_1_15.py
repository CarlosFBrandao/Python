import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice1 = math.hypot(vertice2.getx() - vertice1.getx(),
                                    (vertice2.gety() - vertice1.gety()))
        self.__vertice2 = math.hypot(vertice3.getx() - vertice2.getx(),
                                    (vertice3.gety() - vertice2.gety()))
        self.__vertice3 = math.hypot(vertice3.getx() - vertice1.getx(),
                                    (vertice3.gety() - vertice1.gety()))

    def perimeter(self):
        return self.__vertice1 + self.__vertice2 + self.__vertice3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
