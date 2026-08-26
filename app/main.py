import math


class Vector:
    # write your code here
    def __init__(self, coor_x: int | float, coor_y: int | float) -> None:
        self.x = round(coor_x, 2)
        self.y = round(coor_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            coor_x=self.x + other.x,
            coor_y=self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            coor_x=self.x - other.x,
            coor_y=self.y - other.y
        )

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                coor_x=self.x * other,
                coor_y=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        if start_point == (0, 0) and end_point == (0, 0):
            raise ValueError("Start or end point is equal to 0")
        return Vector(
            coor_x=end_point[0] - start_point[0],
            coor_y=end_point[1] - start_point[1]
        )

    # @staticmethod
    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(
            coor_x=self.x / length,
            coor_y=self.y / length
        )

    def angle_between(self, other: "Vector") -> int | float:
        length_of_vector_1 = self.get_length()
        length_of_vector_2 = other.get_length()

        print(length_of_vector_1)
        print(length_of_vector_2)

        if length_of_vector_1 == 0 or length_of_vector_2 == 0:
            raise ValueError("Length of vector is equal to 0")

        multiply = self.__mul__(other)

        cos_theta = multiply / (length_of_vector_1 * length_of_vector_2)

        cos_theta = max(-1.0, min(1.0, cos_theta))

        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        positive_y_axis = Vector(0, 1)
        dot_prod = self.__mul__(positive_y_axis)
        mag_self = self.get_length()
        mag_positive_y = positive_y_axis.get_length()
        cos_theta = dot_prod / (mag_self * mag_positive_y)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_radians = math.acos(cos_theta)
        angle_degrees = math.degrees(angle_radians)

        return round(angle_degrees)

    def rotate(self, degrees: int | float) -> "Vector":
        radians = math.radians(degrees)

        # Apply rotation matrix
        rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(rotated_x, rotated_y)
