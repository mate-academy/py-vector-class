import math


class Vector:
    def __init__(self, x_num: int, y_num: int) -> None:
        self.x = round(x_num, 2)
        self.y = round(y_num, 2)

    def __add__(self, other: list) -> None:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: list) -> None:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: list) -> None:
        if type(other) == int or type(other) == float:
            return Vector(self.x * other, self.y * other)
        dot_product = (self.x * other.x) + (self.y * other.y)
        return dot_product

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: int,
                                    end_point: int) -> None:
        return cls(end_point[0]
                   - start_point[0],
                   end_point[1]
                   - start_point[1])

    def get_length(self) -> list:
        return math.sqrt((self.x ** 2) + (self.y**2))

    def get_normalized(self) -> None:
        return Vector(round
                      (self.x
                       / self.get_length()
                       , 2),
                      round
                      (self.y
                       / self.get_length()
                       , 2))

    def angle_between(self, other: list) -> int:
        cos = math.acos(self * other
                        / (self.get_length()
                           * other.get_length()))
        degree = round(math.degrees(cos))
        return degree

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, num: int) -> None:
        sin = math.sin(math.radians(num))
        cos = math.cos(math.radians(num))
        x_vec = (cos * self.x) - (sin * self.y)
        y_vec = sin * self.x + cos * self.y
        return Vector(x_vec, y_vec)
