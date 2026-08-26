from typing import Union
import math


class Vector:
    def __init__(
            self, x_coord: Union[int, float],
            y_coord: Union[int, float]
    ) -> None:
        if not (
                isinstance(x_coord, (int, float))
                and isinstance(y_coord, (int, float))
        ):
            raise TypeError("Unsupported type.")
        else:
            self.x = round(x_coord, 2)
            self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Unsupported type.")
        else:
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Unsupported type.")
        else:
            return Vector(
                self.x - other.x,
                self.y - other.y
            )

    def __mul__(
            self, other: Union[int, float, "Vector"]
    ) -> Union[int, float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            return ((self.x * other.x) + (self.y * other.y))
        else:
            raise TypeError("Unsupported type.")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        if not (
                isinstance(start_point, tuple)
                and isinstance(end_point, tuple)
        ):
            raise TypeError("Unsupported type.")
        elif len(start_point) < 2 or len(end_point) < 2:
            raise TypeError("Small tuple.")
        else:
            return cls(
                x_coord=end_point[0] - start_point[0],
                y_coord=end_point[1] - start_point[1]
            )

    def get_length(self) -> Union[int, float]:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> "Vector":
        if self.get_length() == 0:
            raise TypeError("Length is zero.")
        else:
            return Vector(
                x_coord=self.x / self.get_length(),
                y_coord=self.y / self.get_length()
            )

    def angle_between(self, other: "Vector") -> Union[int, float]:
        if not isinstance(other, Vector):
            raise TypeError("Unsupported type.")
        elif (self.get_length() == 0 or other.get_length() == 0):
            raise TypeError("Length is zero.")
        else:
            cos_theta = ((self.x * other.x + self.y * other.y)
                         / (math.sqrt(self.x ** 2 + self.y ** 2)
                            * math.sqrt(other.x ** 2 + other.y ** 2)))
            theta = math.acos(cos_theta)
        return round(math.degrees(theta))

    def get_angle(self) -> Union[int, float]:
        un_y = Vector(0, 1)
        return round(self.angle_between(un_y))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta
        return Vector(x_new, y_new)
