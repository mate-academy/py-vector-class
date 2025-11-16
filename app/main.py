from typing import Union


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,
                scalar: Union['Vector', float, int]
                ) -> Union[float, 'Vector', int]:
        if isinstance(scalar, Vector):
            return self.x * scalar.x + self.y * scalar.y
        return Vector(round(self.x * scalar, 2), round(self.y * scalar, 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> 'Vector':
        x_diff = end_point[0] - start_point[0]
        y_diff = end_point[1] - start_point[1]
        return cls(x_diff, y_diff)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> 'Vector':
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: 'Vector') -> float:
        from math import acos, degrees
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0.0
        cos_angle = dot_product / length_product
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_rad = acos(cos_angle)
        angle_deg = degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> float:
        from math import atan2, degrees
        angle_rad = atan2(self.x, self.y)
        angle_deg = degrees(angle_rad)
        if angle_deg < 0:
            angle_deg = -angle_deg
        return round(angle_deg)

    def rotate(self, angle: float) -> 'Vector':
        from math import cos, sin, radians
        angle_rad = radians(angle)
        new_x = self.x * cos(angle_rad) - self.y * sin(angle_rad)
        new_y = self.x * sin(angle_rad) + self.y * cos(angle_rad)
        return Vector(round(new_x, 2), round(new_y, 2))
