from __future__ import annotations
import math


class Vector:
    """
    A class to represent a 2D vector originating from the point (0, 0) to (x, y).

    Attributes:
        x (float): The x-coordinate of the vector, rounded to two decimals.
        y (float): The y-coordinate of the vector, rounded to two decimals.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initializes the Vector object with x and y coordinates.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
        """
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector: Vector) -> Vector:
        """
        Adds two vectors and returns the resulting vector.

        Args:
            vector (Vector): The vector to add.

        Returns:
            Vector: A new vector that is the sum of the current vector and the provided vector.
        """
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        """
        Subtracts one vector from another and returns the resulting vector.

        Args:
            vector (Vector): The vector to subtract.

        Returns:
            Vector: A new vector that is the difference between the current vector and the provided vector.
        """
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector: Vector | float) -> Vector | float:
        """
        Multiplies the vector by either another vector or a scalar value.

        Args:
            vector (Vector | float): The vector to calculate the dot product with, or the scalar to multiply by.

        Returns:
            Vector | float: If `vector` is a vector, returns the dot product.
                            If `vector` is a scalar, returns a new vector scaled by the scalar.
        """
        if isinstance(vector, Vector):
            return self.x * vector.x + self.y * vector.y

        return Vector(self.x * vector, self.y * vector)

    def get_length(self) -> float:
        """
        Calculates the length (magnitude) of the vector.

        Returns:
            float: The length of the vector.
        """
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        """
        Returns a normalized (unit length) copy of the vector.

        Returns:
            Vector: A new vector that is the normalized version of the current vector.
        """
        length = self.get_length()
        norm_x = self.x / length
        norm_y = self.y / length
        return Vector(norm_x, norm_y)

    def angle_between(self, vector: Vector) -> int:
        """
        Calculates the angle between the current vector and another vector in degrees.

        Args:
            vector (Vector): The vector to calculate the angle with.

        Returns:
            int: The angle between the two vectors, rounded to the nearest degree.
        """
        prod = self * vector
        len_prod = self.get_length() * vector.get_length()
        degree = math.degrees(math.acos(prod / len_prod))
        return round(degree)

    def get_angle(self) -> int:
        """
        Returns the angle between the current vector and the positive Y-axis in degrees.

        Returns:
            int: The angle between the vector and the positive Y-axis, rounded to the nearest degree.
        """
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        """
        Rotates the vector by a specified angle in degrees and returns the resulting vector.

        Args:
            angle (int): The angle by which to rotate the vector, in degrees.

        Returns:
            Vector: A new vector that is the result of rotating the current vector by the specified angle.
        """
        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vector(x, y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float], end_point: tuple[float, float]) -> Vector:
        """
        Creates a vector given two points: a start point and an end point.

        Args:
            start_point (tuple[float, float]): The coordinates of the start point.
            end_point (tuple[float, float]): The coordinates of the end point.

        Returns:
            Vector: A new vector that represents the direction and distance from the start point to the end point.
        """
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])
