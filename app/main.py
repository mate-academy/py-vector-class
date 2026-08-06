import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: object) -> object:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object) -> object:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | object) -> object | float:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        return self.x * other.x + self.y * other.y  # dot product of 2 vectors

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> object:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return math.sqrt(self.x**2 + self.y**2)  # vector magnitude

    def get_normalized(self) -> object:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: object) -> int:
        magnitude_other_vector = round(math.sqrt(other.x**2 + other.y**2), 1)
        cos_a = (self * other) / (self.get_length() * magnitude_other_vector)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        if self.y < 0:
            return round(
                180 - math.degrees(math.atan(abs(self.x / self.y)))
            )
        return round(math.degrees(math.atan(abs(self.x / self.y))))

    def rotate(self, degrees: int) -> object:
        degrees = math.radians(degrees)
        new_x = self.x * math.cos(degrees) - self.y * math.sin(degrees)
        new_y = self.x * math.sin(degrees) + self.y * math.cos(degrees)
        return Vector(new_x, new_y)
