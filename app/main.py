import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector" | int | float) -> "Vector":
        if isinstance(other, Vector):
            result_x = self.x * other.x 
            result_y = self.y * other.y
            return result_x + result_y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> "Vector":
        return (self.x**2 + self.y**2) ** (1/2)

    def get_normalized(self) -> "Vector":
        self_length = self.get_length()
        return Vector(self.x/self_length, self.y/self_length)

    def angle_between(self, other: "Vector") -> int:
        result = self.__mul__(other)/(self.get_length() * other.get_length())
        result = min(1, max(-1, result))
        rad_angle = math.acos(result)
        return round(math.degrees(rad_angle))

