import math


class Vector:
    def __init__(self, х_coord: int | float, y_coord: int | float) -> None:
        self.x = round(х_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        # just by adding their x and y components separately:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        # just by subtracting their x and y components separately:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(
            self, other: int | float or "Vector"
    ) -> "Vector" or int | float:
        # Vector multiplied by number x*num, y*num
        # Vector multiplied by Vector = dot_product
        # self.x * other.x + self.y * other.y
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        # The directional vector can be determined
        # by subtracting the start from the end point.
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        #  square root of x2 + y2 (by the Pythagorean Theorem)
        v_length = math.sqrt(
            self.x**2 + self.y**2
        )
        return v_length

    def get_normalized(self) -> "Vector":
        # The normalized vector of X is a vector
        # in the same direction but with norm (length) 1
        # formula = x / length of vector, y / length of vector
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: "Vector") -> int | float:
        # To find the angle θ between two vectors,
        # start with the formula for finding that angle's cosine
        # cos_a = dot_product(multiplied vectors) /
        # (length_of_1_vector *  length_of_2_vector)
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        angle = round(
            math.degrees(math.acos(cos_a))
        )
        return angle

    def get_angle(self) -> int | float:
        # Returns angle between current vector and positive Y axis.
        positive_y_axis = Vector(0, 1)
        angle = self.angle_between(positive_y_axis)
        return angle

    def rotate(self, degrees: int | float) -> "Vector":
        theta = math.radians(degrees)
        return Vector(
            math.cos(theta) * self.x - math.sin(theta) * self.y,
            math.sin(theta) * self.x + math.cos(theta) * self.y
        )
