import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | "Vector") -> float | "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError(
            "Multiplication only supported with int, float, or Vector"
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        coord_x = end_point[0] - start_point[0]
        coord_y = end_point[1] - start_point[1]
        return cls(coord_x, coord_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return 0
        cos_a = dot_product / (len_self * len_other)
        cos_a = max(min(cos_a, 1), -1)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_a = self.y / length
        cos_a = max(min(cos_a, 1), -1)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = (
            self.x * math.cos(radians) - self.y * math.sin(radians)
        )
        new_y = (
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
        return Vector(new_x, new_y)
