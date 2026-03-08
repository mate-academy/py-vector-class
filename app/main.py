import math


class Vector:
    def __init__(self, vector_x: int | float, vector_y: int | float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if not isinstance(other, Vector):
            return Vector(
                self.x * other,
                self.y * other
            )
        return sum([self.x * other.x, self.y * other.y])

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(self.__mul__(other)
                          / (self.get_length() * other.get_length()))
            )
        )

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, rotation: int) -> Vector:
        rotation = math.radians(rotation)
        return Vector(
            self.x * math.cos(rotation) - self.y * math.sin(rotation),
            self.x * math.sin(rotation) + self.y * math.cos(rotation)
        )
