import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: type) -> type:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )
    """Addition of two Vectors and return Vector"""

    def __sub__(self, other: type) -> float:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )
    """Subtraction of two Vectors and return Vector.

"""

    def __mul__(self, other: type) -> float:
        if not isinstance(other, Vector):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        else:
            return self.x * other.x + self.y * other.y
        """
        Multiplying Vector on a number and return another Vector.
        or
        Multiplying Vector on Vector and return their dot product.
        """

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> type:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )
        """Takes (start_point) - tuple of point coordinates,
            start of the vector,
            (end_point) - tuple of point coordinates, end of the vector
            It returns Vector."""

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    """Returns length of the vector."""
    def get_normalized(self) -> type:
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )
    """Returns normalized copy of vector."""

    def angle_between(self, other: type) -> int:
        if isinstance(other, Vector):
            cos_a = (self.x * other.x + self.y * other.y) / \
                    (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))
    """Takes vector and returns angle between current vector
        and vector in integer degrees."""

    def get_angle(self) -> int:
        cos_a = (self.x * 0 + self.y * 1) / \
                (self.get_length() * ((0 ** 2 + 1 ** 2) ** 0.5))
        return round(math.degrees(math.acos(cos_a)))
    """Returns angle between current vector and positive Y axis."""

    def rotate(self, degrees: int) -> type:
        cs = math.cos(math.radians(degrees))
        sn = math.sin(math.radians(degrees))
        return Vector(
            x=self.x * cs - self.y * sn,
            y=self.x * sn + self.y * cs
        )
    """Takes degrees that is integer rotation degrees
        It returns rotated Vector by degrees."""
