import math


class Vector:
    def __init__(self, x_val: float, y_val: float) -> None:
        self.x = round(x_val, 2)
        self.y = round(y_val, 2)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        angle = math.acos((self * other)
                          / (self.get_length() * other.get_length()))
        return round(math.degrees(angle))

    def get_angle(self) -> float:
        other = Vector(0, self.y)
        angle = self.angle_between(other)
        if self.y < 0:
            angle = 180 - angle
        return angle

    def rotate(self, angle: int) -> Vector:
        angle_radians = math.radians(angle)
        x_rotatad = round(
            math.cos(angle_radians) * self.x
            - math.sin(angle_radians) * self.y,
            2)
        y_rotated = round(
            math.sin(angle_radians) * self.x
            + math.cos(angle_radians) * self.y,
            2)
        return Vector(x_rotatad, y_rotated)
