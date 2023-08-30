import math


class Vector:

    def __init__(self, first: float, second: float) -> None:
        self.x = round(first, 2)
        self.y = round(second, 2)

    def __add__(self, other: any) -> any:
        other_x = (self.x + other.x)
        other_y = self.y + other.y
        return Vector(other_x, other_y)

    def __sub__(self, other: any) -> any:
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return Vector(sub_x, sub_y)

    def __mul__(self, other: any) -> any:
        if isinstance(other, Vector):
            mul_x = self.x * other.x
            mul_y = self.y * other.y
            return mul_x + mul_y
        mul_x = self.x * other
        mul_y = self.y * other
        return Vector(mul_x, mul_y)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> any:
        start_x, start_y = start
        end_x, end_y = end
        new_x = end_x - start_x
        new_y = end_y - start_y
        return Vector(new_x, new_y)

    def get_length(self, other_x: int = 0, other_y: int = 0) -> any:
        return (((self.x - other_x) ** 2) + ((self.y - other_y) ** 2)) ** 0.5

    def get_normalized(self) -> int:
        length = self.get_length()
        new_x = self.x / length
        new_y = self.y / length
        return Vector(new_x, new_y)

    def angle_between(self, vector: any) -> int:
        dot_product = self.x * vector.x + self.y * vector.y
        length_product = self.get_length() * vector.get_length()
        cos_angle = dot_product / length_product
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        res = math.atan2(self.x, self.y)
        if round(math.degrees(res)) < 0:
            return -round(math.degrees(res))
        return round(math.degrees(res))

    def rotate(self, num: int) -> any:
        rad = num * math.pi / 180
        sin = math.sin(rad)
        cos = math.cos(rad)
        new_x = self.x * cos - self.y * sin
        new_y = self.x * sin + self.y * cos
        return Vector(new_x, new_y)
