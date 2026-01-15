import math
from typing import Union


class Vector:
    def __init__(self, end_x: float, end_y: float) -> None:
        self.x = round(end_x, 2)
        self.y = round(end_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            # Dot product of two vectors
            return round(self.x * other.x + self.y * other.y, 14)
        elif isinstance(other, (int, float)):
            # Scalar multiplication
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: 'Vector' "
                f"and '{type(other)}'"
            )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_angle = dot_product / length_product
        cos_angle = max(min(cos_angle, 1), -1)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(
            round(new_x, 2),
            round(new_y, 2)
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
