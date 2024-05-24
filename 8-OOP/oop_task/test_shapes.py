import shapes
import math


def test_cube():
    cube_20 = shapes.cube("red", 20, 0, 0, 0)
    assert cube_20.area() == 20**2
    assert cube_20.volume() == 20**3
    assert cube_20.surface_area() == (20**2) * 6
    assert cube_20.perimeter() == 20 * 4


def test_sphere():
    sphere_20 = shapes.sphere("blue", 20, 0, 0, 0)
    pi = 3.14
    assert sphere_20.area() == pi * (10**2)
    assert sphere_20.volume() == 4 / 3 * pi * (10**2)
    assert sphere_20.surface_area() == 4 * pi * (10**2)
    assert sphere_20.perimeter() == 2 * pi * 10


def test_bipyramid():
    bipyramid_20 = shapes.equilateral_triangular_bipyramid("cyan", 20, 0, 0, 0)
    assert bipyramid_20.area() == 1 / 2 * 20 * math.sqrt(10**2 + 20**2)
    assert bipyramid_20.volume() == 1 / 3 * (
        1 / 2 * 20 * math.sqrt(10**2 + 20**2)
    ) * math.sqrt(10**2 + 20**2)
    assert (
        bipyramid_20.surface_area()
        == math.sqrt(
            (math.sqrt(10**2 + 20**2) / 2) ** 2 + math.sqrt(10**2 + 20**2) ** 2
        )
        * 20
        * (1 / 2)
        * 6
    )
    assert bipyramid_20.perimeter() == 20 * 3


if __name__ == "__main__":
    cube_20 = shapes.cube("red", 20, 0, 0, 0)
    print(cube_20.area())
