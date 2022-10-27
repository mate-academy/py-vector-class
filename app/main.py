import math


class Vector:
    def __init__(self, ax_x: float, ax_y: float) -> None:
        self.x = round(ax_x, 2)
        self.y = round(ax_y, 2)

    def __add__(self, other: object) -> object:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object) -> object:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> object:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

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

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        inv_lenght = 1 / self.get_length()
        return Vector(self.x * inv_lenght, self.y * inv_lenght)

    def angle_between(self, other: object) -> int:
        self_lenght = self.get_length()
        other_lenght = other.get_length()
        dot_prod = self * other
        cos_fi = dot_prod / (self_lenght * other_lenght)
        fi = round(math.degrees(math.acos(cos_fi)))
        return fi

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> object:
        angle_rad = math.radians(angle)
        cs = math.cos(angle_rad)
        sn = math.sin(angle_rad)
        rx = self.x * cs - self.y * sn
        ry = self.x * sn + self.y * cs
        return Vector(rx, ry)
