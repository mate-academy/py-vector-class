import math
from typing import Any


class Vector:

    def __init__(self, x_cor: float, y_cor : float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(round((self.x * other), 2), round((self.y * other), 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        start_point_list = list(start_point)
        end_point_list = list(end_point)
        return cls(round(end_point_list[0] - start_point_list[0], 2),
                   round(end_point_list[1] - start_point_list[1], 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = 1 / self.get_length()
        return Vector.__mul__(self, length)

    def angle_between(self, other: "Vector") -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / (math.sqrt(self.x ** 2 + self.y ** 2))
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> "Vector":
        degrees_r = math.radians(degrees)
        res = self.x
        self.x = round(self.x * math.cos(degrees_r)
                       - self.y * math.sin(degrees_r), 2)
        self.y = round(res * math.sin(degrees_r)
                       + self.y * math.cos(degrees_r), 2)
        return self


vector = Vector(-2.343, 8.008)
print(vector.x)  # -2.34
print(vector.y)  # 8.0

vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)
vector3 = vector1 + vector2
print(isinstance(vector3, Vector) is True)
print(vector3.x)  # 1
print(vector3.y)  # 7

vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)
vector3 = vector1 - vector2
print(isinstance(vector3, Vector) is True)
print(vector3.x)  # 3
print(vector3.y)  # 1

vector1 = Vector(2, 4)
vector2 = vector1.__mul__(3.743)
print(isinstance(vector2, Vector) is True)
print(vector2.x)  # 7.49
print(vector2.y)  # 14.97

vector1 = Vector(2.11, 4.55)
vector2 = Vector(-3.51, 10.33)
print(vector1.__mul__(vector2))  # 39.5954

start_point = (5.2, 2.6)
end_point = (10.7, 6)
vector = Vector.create_vector_by_two_points(start_point, end_point)
print(isinstance(vector, Vector) is True)
print(vector.x)  # == 5.5
print(vector.y)  # 3.4

vector = Vector(2, 4)
print(vector.get_length())  # 4.47213595499958

vector1 = Vector(13, -4)
vector1.get_length()  # 13.6

vector2 = vector1.get_normalized()

print(vector2.x)  # 0.96
print(vector2.y)  # -0.29
print(vector2.get_length())  # 1.0

vector1 = Vector(13, -4)
vector2 = Vector(-6, -11)
print(vector1.angle_between(vector2))  # 102

vector = Vector(33, 8)
print(vector.get_angle())  # 76

vector = Vector(33, 8)
vector2 = vector.rotate(45)
print(vector2.x)  # 17.68
print(vector2.y)  # 28.99 (18.15)
