from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis : float, y_axis : float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, another : Vector) -> Vector:
        return Vector(self.x + another.x, self.y + another.y)

    def __sub__(self, another : Vector) -> Vector:
        return Vector(self.x - another.x, self.y - another.y)

    def __mul__(self, another : Vector | float) -> Vector | float:
        if getattr(another, "x", 0):
            return self.x * another.x + self.y * another.y
        else:
            return Vector(self.x * another, self.y * another)

    @classmethod
    def create_vector_by_two_points(cls, start_point : tuple,
                                    end_point: tuple) -> Vector:
        start_point_list = []
        for i in start_point:
            start_point_list.append(i)
        end_point_list = []
        for i in end_point:
            end_point_list.append(i)
        return Vector(end_point_list[0] - start_point_list[0],
                      end_point_list[1] - start_point_list[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        veclen = self.get_length()
        return Vector(self.x / veclen, self.y / veclen)

    def angle_between(self, another : Vector) -> float:
        dot_prod = self * another
        mag_a = self.get_length()
        mag_b = another.get_length()
        angle_cos = dot_prod / (mag_a * mag_b)
        angle_rad = math.acos(angle_cos)
        return math.ceil(math.degrees(angle_rad))

    def get_angle(self) -> float:
        # angle_cos = self.x / self.get_length()
        # angle_rad = math.acos(angle_cos)
        # return math.degrees(angle_rad)
        return round(math.degrees(math.atan2(abs(self.x), self.y)))

    def rotate(self, degrees : float) -> Vector:
        ang_rad = math.radians(degrees)
        result_x = self.x * math.cos(ang_rad) - self.y * math.sin(ang_rad)
        result_y = self.x * math.sin(ang_rad) + self.y * math.cos(ang_rad)
        return Vector(result_x, result_y)
