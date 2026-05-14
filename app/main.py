import math
from typing import Union


Number = Union[int, float]


class Vector:
    """Two-dimensional vector with basic vector operations."""

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        """Return the sum of two vectors."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        """Return the difference between two vectors."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", Number]) -> Union["Vector", float]:
        """
        Multiply vector by scalar or calculate dot product.

        If `other` is a number, returns scaled vector.
        If `other` is a vector, returns dot product.
        """
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        """Create vector from two points."""
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        """Return vector length."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        """Return normalized vector."""
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        """Return angle in degrees between two vectors."""
        dot = self.x * other.x + self.y * other.y
        denominator = self.get_length() * other.get_length()

        cos_a = dot / denominator
        cos_a = max(-1.0, min(1.0, cos_a))

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        """Return angle between vector and Y-axis in degrees."""
        length = self.get_length()
        cos_a = self.y / length
        cos_a = max(-1.0, min(1.0, cos_a))

        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> "Vector":
        """Return vector rotated by given degrees."""
        theta = math.radians(degrees)

        new_x = (
            self.x * math.cos(theta)
            - self.y * math.sin(theta)
        )
        new_y = (
            self.x * math.sin(theta)
            + self.y * math.cos(theta)
        )

        return Vector(new_x, new_y)
