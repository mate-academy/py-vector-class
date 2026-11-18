import math


class Vector:

    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        self.x = round(pos_x, 2)
        self.y = round(pos_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[float | int, float | int],
            end_point: tuple[float | int, float | int]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(), self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> float | int:
        return round(math.degrees(math.acos(
            (self * other) / (self.get_length() * other.get_length())))
        )

    def get_angle(self) -> float | int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: float | int) -> Vector:
        rad = math.radians(angle)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)

        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a

        return Vector(new_x, new_y)
