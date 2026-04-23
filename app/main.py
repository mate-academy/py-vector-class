import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self, other: "Vector | int | float"
    ) -> "float | Vector | None":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return None

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        mag = self.get_length()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)

    def angle_between(self, other: "Vector") -> float:
        dot = self * other
        mags = self.get_length() * other.get_length()
        cos_a = max(-1.0, min(1.0, dot / mags))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        axis_y = Vector(0, 1)
        return round(self.angle_between(axis_y))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)
