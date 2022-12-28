from __future__ import annotations


class Vector:
    x = None
    y = None

    # start_point = None
    # end_point = None

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + round(other.x, 2),
            y=self.y + round(other.y, 2),
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - round(other.x, 2),
            y=self.y - round(other.y, 2),
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                x=round(self.x * other, 2),
                y=round(self.y * other, 2),
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return cls(cls.x, cls.y)

    def get_length(self) -> float:
        return round((self.x**2 + self.y**2) ** 0.5, 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )


    def angle_between(self, vector):


vector1 = Vector(13, -4)
vector2 = Vector(-6, -11)

v1 = vector1.get_normalized()
print(v1)