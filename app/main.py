from __future__ import annotations
import math


class Vector:
    """A class to represent a 2D vector.

    :param x_pos: The x-coordinate of the vector.
    :type x_pos: RealNum
    :param y_pos: The y-coordinate of the vector.
    :type y_pos: RealNum
    """

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Coordinates,
        end_point: Coordinates
    ) -> Vector:
        """Creates a Vector object from two points.

        :param start_point: The starting point of the vector.
        :type start_point: Coordinates
        :param end_point: The ending point of the vector.
        :type end_point: Coordinates
        :return: A new Vector object.
        :rtype: Vector
        """
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def __init__(self, x_pos: RealNum, y_pos: RealNum) -> None:
        """Initializes a Vector object.

        :param x_pos: The x-coordinate of the vector.
        :type x_pos: RealNum
        :param y_pos: The y-coordinate of the vector.
        :type y_pos: RealNum
        """
        self.x = round(x_pos, 2)
        self.y = round(y_pos, 2)

    def __add__(self, other: Vector) -> Vector:
        """Adds two Vector objects.

        :param other: The other Vector object to add.
        :type other: Vector
        :return: A new Vector object representing the sum.
        :rtype: Vector
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        """Subtracts two Vector objects.

        :param other: The other Vector object to subtract.
        :type other: Vector
        :return: A new Vector object representing the difference.
        :rtype: Vector
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | RealNum) -> RealNum | Vector:
        """Multiplies a Vector by another Vector or a real number.

        If other is a Vector, it returns the dot product.
        If other is a real number, it returns a new scaled Vector.

        :param other: The other Vector or real number to multiply by.
        :type other: Vector | RealNum
        :return: The dot product or a new scaled Vector.
        :rtype: RealNum | Vector
        """
        if isinstance(other, Vector):

            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    def get_length(self) -> RealNum:
        """Calculates the length of the vector.

        :return: The length of the vector.
        :rtype: RealNum
        """
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        """Normalizes the vector.

        :return: A new normalized Vector.
        :rtype: Vector
        """
        vector_len = self.get_length()

        return Vector(
            self.x / vector_len,
            self.y / vector_len
        )

    def angle_between(self, other: Vector) -> int:
        """Calculates the angle between two vectors in degrees.

        :param other: The other Vector object.
        :type other: Vector
        :return: The angle between the two vectors in degrees.
        :rtype: int
        """
        return round(math.degrees(math.acos(
            self.__mul__(other)
            / (self.get_length() * other.get_length())
        )))

    def get_angle(self) -> int:
        """Calculates the angle of the vector in degrees.

        :return: The angle of the vector in degrees.
        :rtype: int
        """
        return round(math.degrees(math.acos(
            self.y / self.get_length()
        )))

    def rotate(self, angle: int) -> Vector:
        """Rotates the vector by a given angle in degrees.

        :param angle: The angle to rotate the vector by in degrees.
        :type angle: int
        :return: A new rotated Vector.
        :rtype: Vector
        """
        rad_angle = math.radians(angle)
        sine = math.sin(rad_angle)
        cosine = math.cos(rad_angle)

        return Vector(
            self.x * cosine - self.y * sine,
            self.x * sine + self.y * cosine
        )


RealNum = int | float
Coordinates = tuple[RealNum, RealNum]
