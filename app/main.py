import math
from typing import Union


class Vector:

    def __init__(self, x_coor: float, y_coor: float) -> None:
        self.x = round(x_coor, 2)
        self.y = round(y_coor, 2)

    def __add__(self, other: "Vector") -> "Vector":
        x_coor = self.x + other.x
        y_coor = self.y + other.y
        return Vector(x_coor, y_coor)

    def __sub__(self, other: "Vector") -> "Vector":
        x_coor = self.x - other.x
        y_coor = self.y - other.y
        return Vector(x_coor, y_coor)

    def __mul__(self, other: Union["Vector", float]) -> Union[float, "Vector"]:

        if isinstance(other, Vector):
            x_coor = self.x * other.x
            y_coor = self.y * other.y

            return x_coor + y_coor

        else:
            x_coor = self.x * other
            y_coor = self.y * other

            return Vector(x_coor, y_coor)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":

        x1, y1 = start_point
        x2, y2 = end_point
        x_coor = x2 - x1
        y_coor = y2 - y1

        return cls(x_coor, y_coor)

    def get_length(self, x_coor: float = None, y_coor: float = None) -> float:
        if x_coor:
            return (x_coor ** 2 + y_coor ** 2) ** 0.5

        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        module_vector = self.get_length()
        x_coor = self.x / module_vector
        y_coor = self.y / module_vector

        return Vector(x_coor, y_coor)

    def angle_between(self, other: "Vector") -> int:
        magnitude_vec_1 = self.get_length()
        magnitude_vec_2 = self.get_length(other.x, other.y)

        dot_product = self * other
        cos0 = dot_product / (magnitude_vec_1 * magnitude_vec_2)

        return math.ceil(math.degrees(math.acos(cos0)))

    def get_angle(self) -> float:
        angle_radians = math.atan2(self.x, self.y)

        return int(math.degrees(angle_radians)) * -1

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        x_coor = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_coor = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(x_coor, y_coor)
