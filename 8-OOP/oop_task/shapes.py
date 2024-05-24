import math


class shape:
    def __init__(self, colour, diameter, x=0, y=0, z=0):
        self.colour = colour
        self.center = (x, y, z)
        self.diameter = diameter

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError("Diameter can't be negative")
        self._diameter = diameter

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        for i in center:
            if str(i).isalpha():
                raise ValueError("Diameter can't be negative")
        self._center = center

    def surface_count(self):
        if type(self) is cube or type(self) is equilateral_triangular_bipyramid:
            return 6
        else:
            return None


class sphere(shape):
    def area(self, pi=3.14):
        return pi * ((self._diameter / 2) ** 2)

    def perimeter(self, pi=3.14):
        return self._diameter * pi

    def surface_area(self, pi=3.14):
        return 4 * ((self._diameter / 2) ** 2) * pi

    def volume(self, pi=3.14):
        return 4 / 3 * pi * (self._diameter / 2) ** 2


class cube(shape):
    def area(self):
        return self._diameter**2

    def perimeter(self):
        return self._diameter * 4

    def surface_area(self):
        return self.area() * 6

    def volume(self):
        return self._diameter**3


class equilateral_triangular_bipyramid(shape):
    def height(self):
        return math.sqrt((self._diameter / 2) ** 2 + self._diameter**2)

    def perimeter(self):
        return self._diameter * 3

    def surface_area(self):
        return (
            math.sqrt((self.height() / 2) ** 2 + self.height() ** 2)
            * self._diameter
            * (1 / 2)
            * 6
        )

    def area(self):
        return 1 / 2 * self._diameter * self.height()

    def volume(self):
        return 1 / 3 * self.area() * self.height()
