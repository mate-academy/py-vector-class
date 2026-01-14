from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float = 0.0, y_coord: float = 0.0) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(x_coord=(self.x + other.x),
                          y_coord=(self.y + other.y))
        else:
            raise TypeError((
                f"unsupported operand type(s) for +: 'Vector' and"
                f" {type(other).__name__}"))

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(x_coord=(self.x - other.x),
                          y_coord=(self.y - other.y))
        else:
            raise TypeError((
                f"unsupported operand type(s) for -: 'Vector' and"
                f" {type(other).__name__}"))

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector((self.x * other), self.y * other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: 'Vector'"
                f" and '{type(other).__name__}'"
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        res = []
        for i in range(0, len(end_point)):
            res.append(end_point[i] - start_point[i])

        res = tuple(res)
        return cls(x_coord=round(res[0], 2), y_coord=round(res[1], 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        len_vector = self.get_length()
        if len_vector > 0:
            x_norm = self.x / len_vector
            y_norm = self.y / len_vector
            new_vector = Vector(x_norm, y_norm)
            return new_vector
        else:
            return Vector(0, 0)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        length_self = math.sqrt(self.x ** 2 + self.y ** 2)
        length_other = math.sqrt(other.x ** 2 + other.y ** 2)
        if length_self == 0 or length_other == 0:
            return 0
        cosine_of_the_angle = math.degrees(
            math.acos(dot_product / (length_self * length_other)))
        return round(cosine_of_the_angle)

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = round(self.x * math.cos(radians)
                      - self.y * math.sin(radians), 2)
        new_y = round(self.x * math.sin(radians)
                      + self.y * math.cos(radians), 2)
        return Vector(new_x, new_y)


vector = Vector(-2.343, 8.008)
print(vector.x == -2.34)
print(vector.y == 8.0)

print("*" * 50)

vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)
vector3 = vector1 + vector2

print(isinstance(vector3, Vector) is True)
print(vector3.x == 1)
print(vector3.y == 7)

print("*" * 50)

vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)
vector3 = vector1 - vector2

print(isinstance(vector3, Vector) is True)
print(vector3.x == 3)
print(vector3.y == 1)

print("*" * 50)
vector1 = Vector(2, 4)
vector2 = vector1 * 3.743
print(isinstance(vector2, Vector) is True)
print(vector2.x == 7.49)
print(vector2.y == 14.97)

print("*" * 50)
vector1 = Vector(2.11, 4.55)
vector2 = Vector(-3.51, 10.33)
dot_product = vector1 * vector2
print(dot_product == 39.5954)

print("*" * 50)

print(isinstance(vector, Vector) is True)
start_point = (5.2, 2.6)
end_point = (10.7, 6)

vector = Vector.create_vector_by_two_points(start_point, end_point)

print(isinstance(vector, Vector))
print(vector.x == 5.5)
print(vector.y == 3.4)
print(vector.x)
print(vector.y)

print("*" * 50)
vector = Vector(2, 4)
print(vector.get_length() == 4.47213595499958)

print("*" * 50)
vector1 = Vector(13, -4)
print(vector1.get_length() == 13.6)

vector2 = vector1.get_normalized()

print(vector2.x == 0.96)
print(vector2.y == -0.29)
print(vector2.get_length() == 1.0)

print("*" * 50)
vector1 = Vector(13, -4)
vector2 = Vector(-6, -11)
print(vector1.angle_between(vector2) == 102)
print(vector1.angle_between(vector2))

print("*" * 50)
vector = Vector(33, 8)
print(vector.get_angle() == 76)
print(vector.get_angle())

print("*" * 50)
vector = Vector(33, 8)
vector2 = vector.rotate(45)

print(vector2.x)
print(vector2.y)
print(vector2.x == 17.68)
print(vector2.y == 28.99)
