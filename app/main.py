import math


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: int | float, end_point: int | float
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cos_a = (
            (self.x * other.x + self.y * other.y)
            / (self.get_length() * other.get_length())
        )
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | None:
        if self.x < 0 and self.y < 0:
            return round(abs(math.degrees(math.atan(self.y / self.x)))) + 90
        elif self.x > 0 and self.y > 0:
            return round(abs(math.degrees(math.atan(self.y / self.x))))
        elif self.x == 0:
            return 0
        elif self.x < 0 and self.y > 0:
            return 90 - round(abs(math.degrees(math.atan(self.y / self.x))))

    def rotate(self, degree: float) -> Vector:
        rad = math.radians(degree)
        new_x = round(self.x * math.cos(rad) - self.y * math.sin(rad), 2)
        new_y = round(self.x * math.sin(rad) + self.y * math.cos(rad), 2)
        return Vector(new_x, new_y)
