import math


class Vector:
    # write your code here
    def __init__(self, x_c: float, y_c: float) -> None:
        self.x = round(x_c, 2)
        self.y = round(y_c, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | float | int") -> "float | int | Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> "Vector":

        result_vector = cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1])
        return result_vector

    def get_length(self: "Vector") -> float :

        # return math.sqrt(self.x ** 2 + self.y ** 2)
        return math.hypot(self.x, self.y)

    def get_normalized(self: "Vector") -> "Vector":

        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        # modul_of_vector = self.get_length()
        dot = self.x * other.x + self.y * other.y
        len1 = math.hypot(self.x, self.y)
        len2 = math.hypot(other.x, other.y)
        if len1 == 0 or len2 == 0:
            raise ValueError("Angle is undefined for zero-length vector")
        elif len1 != 0 and len2 != 0:
            cos_angle = max(-1, min(1, dot / (len1 * len2)))
            angle = math.acos(cos_angle)
        return round(math.degrees(angle))

    def get_angle(self) -> int:
        cos_angle = self.y / math.sqrt(self.x ** 2 + self.y ** 2)
        angle = math.acos(cos_angle)
        return round(math.degrees(angle))

    def rotate(self, angle: float | int) -> "Vector":
        cos_angle = math.cos(math.radians(angle))
        sin_angle = math.sin(math.radians(angle))
        x_2 = (self.x * cos_angle) - (self.y * sin_angle)
        y_2 = (self.x * sin_angle) + (self.y * cos_angle)
        return Vector(x_2, y_2)
    pass
