import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other : "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other : "Vector") -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        start_vector = cls(*start_point)
        end_vector = cls(*end_point)
        return end_vector - start_vector

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        normalized_x = round(self.x / length, 2)
        normalized_y = round(self.y / length, 2)

        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_self = self.get_length()
        magnitude_other = other.get_length()
        if magnitude_self != 0 or magnitude_other != 0:
            cos_angle = dot_product / (magnitude_self * magnitude_other)
            angle_radians = math.acos(cos_angle)
            angle_degrees = math.degrees(angle_radians)
            return round(angle_degrees)

    def get_angle(self) -> float:
        y_axis_vector = Vector(0, 1)
        angle = self.angle_between(y_axis_vector)
        return angle

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
