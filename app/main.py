import math


class Vector:
    def __init__(self, x_cor: float, y_cor: float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(round(self.x + other.x, 2),
                      round(self.y + other.y, 2))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: "Vector") -> "Vector" or float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) \
            -> "Vector":
        return cls(round(end_point[0] - start_point[0], 2),
                   round(end_point[1] - start_point[1], 2))

    def get_length(self) -> float:
        return ((self.x) ** 2 + (self.y) ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        x_c = self.x / Vector.get_length(self)
        y_c = self.y / Vector.get_length(self)
        return Vector(round(x_c, 2), round(y_c, 2))

    def angle_between(self, other: "Vector") -> int:
        cos = (Vector.__mul__(self, other)) / \
              (Vector.get_length(self) * abs(Vector.get_length(other)))
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> float:
        return round(math.degrees(math.acos((self.y * 1)
                                            / (Vector.get_length(self)))))

    def rotate(self, angle: int) -> "Vector":
        x_c = round(self.x * math.cos(math.radians(angle))
                    - self.y * math.sin(math.radians(angle)), 2)
        y_c = round(self.x * math.sin(math.radians(angle))
                    + self.y * math.cos(math.radians(angle)), 2)
        return Vector(x_c, y_c)
