from typing import Union
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, vector2: "Vector") -> "Vector":
        return Vector(self.x + vector2.x, self.y + vector2.y)

    def __sub__(self, vector2: "Vector") -> "Vector":
        return Vector(self.x - vector2.x, self.y - vector2.y)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        self_length = self.get_length()
        other_length = other.get_length()
        if self_length != 0 and other_length != 0:
            cos_angle = dot_product / (self_length * other_length)
            angle_rad = math.acos(cos_angle)
            angle_deg = math.degrees(angle_rad)
            return round(angle_deg)
        else:
            return 0

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        return abs(round(angle_deg))

    def rotate(self, degrees: int) -> "Vector":
        angle_rad = math.radians(degrees)
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)
        rotated_x = self.x * cos_theta - self.y * sin_theta
        rotated_y = self.x * sin_theta + self.y * cos_theta
        return Vector(rotated_x, rotated_y)
