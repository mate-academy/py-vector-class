import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "float | int | Vector") -> "float | int | Vector":
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)

        return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple) -> "Vector":

        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot = self * other
        length = self.get_length() * other.get_length()
        cos_angle = dot / length
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, angle: int) -> "Vector":
        radians = math.radians(angle)

        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)

        x_new = self.x * cos_angle - self.y * sin_angle
        y_new = self.x * sin_angle + self.y * cos_angle

        return Vector(x_new, y_new)
