import math


class Vector:
    def __init__(self, xx: float, yy: float) -> None:
        self.xx = round(xx, 2)
        self.yy = round(yy, 2)

    def __add__(self, vec2: Vector) -> Vector:
        return Vector(self.xx + vec2.xx, self.yy + vec2.yy)

    def __sub__(self, vec2: Vector) -> Vector:
        return Vector(self.xx - vec2.xx, self.yy - vec2.yy)

    def __mul__(self, factor: Vector | float) -> float | Vector:
        if isinstance(factor, Vector):
            return self.xx * factor.xx + self.yy * factor.yy
        return Vector(self.xx * factor, self.yy * factor)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.xx ** 2 + self.yy ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.xx / length, self.yy / length)

    def angle_between(self, vec2: Vector) -> float:
        cos_a = (self * vec2) / self.get_length() / vec2.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return Vector.angle_between(self, y_axis)

    def rotate(self, angle: float) -> Vector:
        rad_a = math.radians(angle)
        sin_a = math.sin(rad_a)
        cos_a = math.cos(rad_a)
        return Vector(cos_a * self.xx - sin_a * self.yy,
                      sin_a * self.xx + cos_a * self.yy)
