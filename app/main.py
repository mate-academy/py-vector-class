import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)
        self._x = x_coord
        self._y = y_coord

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | int | float") -> "Vector | float":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self._x * other._x + self._y * other._y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple,
    ) -> "Vector":
        x1, y1 = start_point
        x2, y2 = end_point
        return Vector(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_between(self, other: "Vector") -> int:
        scalar = self.x * other.x + self.y * other.y
        len_1 = math.sqrt(self.x ** 2 + self.y ** 2)
        len_2 = math.sqrt(other.x ** 2 + other.y ** 2)
        cos_a = scalar / (len_1 * len_2)
        return round(math.degrees(math.acos(cos_a)))

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        return Vector(
            self.x * math.cos(rad) - self.y * math.sin(rad),
            self.x * math.sin(rad) + self.y * math.cos(rad),
        )
