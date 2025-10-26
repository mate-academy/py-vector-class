import math
from typing import Union, Tuple


class Vector:
    """
    Representation of a 2D vector with operations such
    as addition, subtraction, scalar multiplication,
    dot product, normalization, and angle calculations.

    This class provides methods to perform common vector
    operations, create vectors based on points, and
    manipulate vector orientation and magnitude.

    """
    def __init__(self, x_point: float, y_point: float) -> None:
        """
        Initialize an instance of the class.

        :param x: The x-coordinate value that
            will be rounded to two decimal
            places during initialization.
        :type x: float
        :param y: The y-coordinate value that
            will be rounded to two decimal
            places during initialization.
        :type y: float
        """
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: "Vector") -> "Vector":
        """
        Adds two Vector instances together.

        This method allows vector addition by adding
        corresponding x and y components of two Vector objects
        and returning a new Vector instance with the summed
        components.

        :param other: The other Vector to be added.
        :type other: Vector
        :return: A new Vector instance resulting from the
            component-wise addition of  the current and
            the provided Vector.
        :rtype: Vector
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        """
        Subtracts one vector from another.

        This method performs the subtraction operation
        between two vectors, where the `other` vector's
        respective x and y components are subtracted from
        the calling vector's x
        and y components, resulting in a new vector.

        :param other: The vector to subtract from the
            current vector.
        :type other: Vector

        :return: A new vector representing the result
            of the subtraction.
        :rtype: Vector
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,
                other: Union["Vector", float, int]
                ) -> Union["Vector", float]:
        """
        Performs multiplication operation between the current
        vector and either another vector or a scalar.
        For vector multiplication, it calculates the dot product.
        For scalar multiplication, it scales the vector.

        :param other: The operand, which can be either another
            Vector instance for a dot product or a scalar
            (float or int) for scaling the vector.
        :returns: The result of the operation. If `other` is a
            vector, the result is a float representing he dot
            product. If `other` is a scalar, the result is
            a new scaled Vector instance.
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]
                                    ) -> "Vector":
        """
        Creates a vector defined by two points.
        This method calculates the vector from the given
        `start_point` to the given `end_point` and
        returns a new instance of Vector.

        :param start_point: A tuple representing the starting
                          point  (x, y) of the vector.
        :param end_point: A tuple representing the ending point
                          (x, y) of the vector.
        :return: A new instance of the Vector class
            representing the calculated vector.
        """
        x_point = end_point[0] - start_point[0]
        y_point = end_point[1] - start_point[1]

        return cls(x_point, y_point)

    def get_length(self) -> float:
        """
        Calculates the length (magnitude) of a vector
        represented by the x and y components using
        the Euclidean formula.

        The method computes the square root of the sum of
        squares of the x and y components of the vector.

        :return: The magnitude of the vector.
        :rtype: float
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        """
        Calculates and returns a normalized version
        of the vector.

        The normalization process scales the vector
        to have a magnitude of 1, without changing its
        direction. If the vector has zero length, a zero
        vector is returned.

        :return: A new `Vector` instance representing
            the normalized vector.
        :rtype: Vector
        """
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        """
        Calculate the angle between the current vector
        and another vector.

        This method calculates the angle in degrees
        between two vectors. The calculation involves
        the dot product of the vectors and their lengths.
        The cosine of the angle is computed,
        bounded to prevent rounding errors, and finally
        converted to degrees. If either vector has zero length,
        the method returns 0 to avoid division by zero.

        :param vector: A vector to calculate the angle against.
        :type vector: Vector
        :return: The angle in degrees between the current
        vector and the specified vector.
        :rtype: int
        """
        dot_product = self * vector
        length_product = self.get_length() * vector.get_length()

        if length_product == 0:
            return 0

        cos_angle = dot_product / length_product
        cos_angle = max(-1, min(1, cos_angle))

        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)

        return round(angle_degrees)

    def get_angle(self) -> int:
        """
        Calculates the angle between the object
        and the y-axis.

        The method computes the angle by determining
        the angle between the current object and a
        vector representing the y-axis. The calculated
        angle is returned as an integer in degrees.

        :return: The angle in degrees between the
            object and the y-axis.
        :rtype: int
        """
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: Union[int, float]) -> "Vector":
        """
        Rotates the vector by a given angle in degrees,
        returning a new rotated vector.

        This method computes the rotation of a vector
        in a two-dimensional plane using the given angle
        (in degrees). It converts the angle from degrees
        to radians and then applies the standard 2D rotation
        matrix transformation on the vector's  coordinates.

        :param degrees: The angle in degrees by which the
            vector should be rotated.
        :return: A new vector instance rotated by the
            specified angle.
        """
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)

        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle

        return Vector(new_x, new_y)
