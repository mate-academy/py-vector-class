import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector | int | float") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        elif isinstance(other, (int, float)):
            return Vector(
                self.x + other,
                self.y + other
            )

    def __sub__(self, other: int | float) -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )
        elif isinstance(other, (int, float)):
            return Vector(
                self.x - other,
                self.y - other
            )

    def __mul__(self, other: "Vector | float | int") -> "Vector | float":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # Залиште це без змін
        elif isinstance(other, (int, float)):
            return Vector(
                round(self.x * other, 4),
                round(self.y * other, 4)
            )

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> "Vector":
        return cls(
            end[0] - start[0],
            end[1] - start[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = round(self.get_length(), 1)
        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, vector: int) -> int:
        length = self.get_length()
        length_vector = vector.get_length()
        return round(
            math.degrees(
                math.acos(self * vector / (length * length_vector))
            )
        )

    def get_angle(self) -> int:
        scalar_product = self.get_length()
        return round(
            math.degrees(
                math.acos(self * Vector(0, 1) / scalar_product)
            )
        )

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x, new_y)
