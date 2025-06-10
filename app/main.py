from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis, y_axis):
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
            dx = end_point[0] - start_point[0]
            dy = end_point[1] - start_point[1]
            return cls(dx, dy)

    def get_length(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            raise ValueError ("It cannot be zero")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other):
        dot_prod = self.x * other.x + self.y * other.y
        length_self = self.get_length()
        length_other = other.get_length()
        cosine_angle = dot_prod / (length_self * length_other)
        cosine_angle = max(-1.0, min(1.0, cosine_angle))
        angle_rad = math.acos(cosine_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self):
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        angle_deg = (360 - angle_deg) % 360
        return round(angle_deg)


    def rotate(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)