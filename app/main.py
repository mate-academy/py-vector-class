import math
from typing import Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        # Dot product with consistent precision
        return round(self.x * other.x + self.y * other.y, 5)

    @classmethod
    def create_vector_by_two_points(
        cls, start: tuple[float, float], end: tuple[float, float]
    ) -> "Vector":
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        # Use round to control the precision of the result
        return round(math.sqrt(self.x**2 + self.y**2), 5)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> int:
        # Calculate the cosine of the angle and clamp it within [-1, 1]
        cos_angle = max(
            -1.0,
            min(1.0, (self * other) / (self.get_length() * other.get_length())),
        )
        # Return the angle rounded to an integer
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        # Rotate the vector and round the results
        rotated_x = round(self.x * cos_angle - self.y * sin_angle, 2)
        rotated_y = round(self.x * sin_angle + self.y * cos_angle, 2)
        return Vector(rotated_x, rotated_y)
