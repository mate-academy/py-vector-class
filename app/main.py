import math
from typing import Self, Union


class Vector:
    def __init__(self, horizontal_coord: float, vertical_coord: float) -> None:
        self.horizontal_coord: float = round(horizontal_coord, 2)
        self.vertical_coord: float = round(vertical_coord, 2)

    def __add__(self, other_vector: Self) -> Self:
        return Vector(self.horizontal_coord + other_vector.horizontal_coord, 
                      self.vertical_coord + other_vector.vertical_coord)

    def __sub__(self, other_vector: Self) -> Self:
        return Vector(self.horizontal_coord - other_vector.horizontal_coord, 
                      self.vertical_coord - other_vector.vertical_coord)

    def __mul__(self, multiplier: Union[Self, float, int]) -> Union[Self, float]:
        if isinstance(multiplier, Vector):
            return (self.horizontal_coord * multiplier.horizontal_coord 
                    + self.vertical_coord * multiplier.vertical_coord)
        return Vector(self.horizontal_coord * multiplier, self.vertical_coord 
                      * multiplier)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float], 
                                    end_point: tuple[float, float]) -> Self:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.horizontal_coord**2 + self.vertical_coord**2)

    def get_normalized(self) -> Self:
        vector_length = self.get_length()
        if vector_length == 0:
            return Vector(0, 0)
        return Vector(self.horizontal_coord / vector_length, self.vertical_coord 
                      / vector_length)

    def angle_between(self, other_vector: Self) -> int:
        length_one = self.get_length()
        length_two = other_vector.get_length()
        if length_one == 0 or length_two == 0:
            return 0
        dot_product = self * other_vector
        cosine_value = max(-1.0, min(1.0, dot_product / (length_one 
                                                         * length_two)))
        angle_in_degrees = math.degrees(math.acos(cosine_value))
        return int(round(angle_in_degrees))

    def get_angle(self) -> int:
        angle_in_radians = math.atan2(self.horizontal_coord, self.vertical_coord)
        angle_in_degrees = math.degrees(angle_in_radians)
        return int(round(angle_in_degrees))

    def rotate(self, rotation_degrees: int) -> Self:
        radians_angle = math.radians(rotation_degrees)
        cos_theta = math.cos(radians_angle)
        sin_theta = math.sin(radians_angle)
        new_horizontal = self.horizontal_coord * cos_theta 
        - self.vertical_coord * sin_theta
        new_vertical = self.horizontal_coord * sin_theta
        + self.vertical_coord * cos_theta
        return Vector(new_horizontal, new_vertical)
