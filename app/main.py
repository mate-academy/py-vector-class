import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float | int:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length = self.get_length() * other.get_length()
        cos_a = dot_product / length
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        rad = math.radians(degrees)
        rotated_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        rotated_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(rotated_x, rotated_y)
