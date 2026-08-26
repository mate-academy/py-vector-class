import math
from typing import Union


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            x_coord=round((self.x + other.x), 2),
            y_coord=round((self.y + other.y), 2)
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            x_coord=round((self.x - other.x), 2),
            y_coord=round((self.y - other.y), 2))

    def __mul__(self, other: Union[int, float, "Vector"]) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector((self.x * other), (self.y * other))
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_points: tuple,
                                    end_points: tuple) -> "Vector":
        return Vector(
            x_coord=end_points[0] - start_points[0],
            y_coord=end_points[1] - start_points[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        else:
            return Vector(0, 0)

    def angle_between(self, other: int | float) -> float:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self != 0 and length_other != 0:
            cos_theta = dot_product / (length_self * length_other)
            theta_rad = math.acos(cos_theta)
            theta_deg = math.degrees(theta_rad)
            return math.ceil(theta_deg)
        else:
            return 0.0

    def get_angle(self) -> float:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)

        return round((abs(angle_deg)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        rotation_matrix = [
            [math.cos(radians), -math.sin(radians)],
            [math.sin(radians), math.cos(radians)]
        ]

        new_x = self.x * rotation_matrix[0][0] + self.y * rotation_matrix[0][1]
        new_y = self.x * rotation_matrix[1][0] + self.y * rotation_matrix[1][1]

        return Vector(new_x, new_y)
