import math
from typing import Union


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self, other: Union['Vector', float, int]
    ) -> Union['Vector', float]:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.x * other, 2), round(self.y * other, 2)
            )
        elif isinstance(other, Vector):
            # Dot product
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> 'Vector':
        """Create a vector from two points."""
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        """Return the length (magnitude) of the vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> 'Vector':
        """Return a normalized copy of the vector."""
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x / length, 2), round(self.y / length, 2)
        )

    def angle_between(self, other: 'Vector') -> int:
        """Return angle between this vector and another in degrees."""
        dot_product = self * other
        magnitude_product = (
            self.get_length() * other.get_length()
        )

        if magnitude_product == 0:
            return 0

        cos_angle = dot_product / magnitude_product
        # Clamp to [-1, 1] to avoid acos numerical errors
        cos_angle = max(-1, min(1, cos_angle))
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)

        return round(angle_degrees)

    def get_angle(self) -> int:
        """Return angle between vector and positive Y axis."""
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> 'Vector':
        """Return a rotated copy of vector by given degrees."""
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)

        # Apply rotation matrix
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a

        return Vector(round(new_x, 2), round(new_y, 2))
