import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "float | Vector") -> "Vector | float":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            result = self.x * other.x + self.y * other.y
            return result
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> float:
        temp = self * other
        cos_a = temp / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> float:
        other = Vector(0, 1)
        angle = self.angle_between(other)
        return angle

    def rotate(self, angle: float) -> "Vector":
        rad = math.radians(angle)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)

