# noqa: VNE001
import math


class Vector:

    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value , 2)
        self.y = round(y_value , 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return (
            Vector(
                end_point[0] - start_point[0], end_point[1] - start_point[1]
            )
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot = self.x * other.x + self.y * other.y
        lengths = self.get_length() * other.get_length()
        return int(round(math.degrees(math.acos(dot / lengths))))

    def get_angle(self) -> float:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)

        return Vector(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle),
        )
