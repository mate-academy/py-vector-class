import math
from typing import Union


class Vector:
    def __init__(self, coordinates_x: float, coordinates_y: float) -> None:
        self.x = round(coordinates_x, 2)
        self.y = round(coordinates_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,
                other: Union[int, float, "Vector"]
                ) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> "Vector":
        return cls(
            coordinates_x=end_point[0] - start_point[0],
            coordinates_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        new_x = self.x / length
        new_y = self.y / length
        return Vector(new_x, new_y)

    def angle_between(self, other_vector: "Vector") -> float:
        length1 = self.get_length()
        length2 = other_vector.get_length()
        dot = self.x * other_vector.x + self.y * other_vector.y
        cos_a = dot / (length1 * length2)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        dot = self.x * y_axis.x + self.y * y_axis.y
        len_self = self.get_length()
        len_y = y_axis.get_length()
        cos_a = dot / (len_self * len_y)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, degrees: int | float) -> "Vector":
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(round(new_x, 2), round(new_y, 2))
