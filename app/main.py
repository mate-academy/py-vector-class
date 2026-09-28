import math


class Vector:

    def __init__(self, x: int, y: int) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        new_x = self.x / self.get_length()
        new_y = self.y / self.get_length()
        return Vector(new_x, new_y)

    def angle_between(self, other: Vector) -> float:
        return round(
            math.degrees(math.acos((self * other)
                                   / (self.get_length()
                                      * other.get_length()))))

    def get_angle(self) -> int:
        return round(math.degrees(math.atan2(abs(self.x), self.y)))

    def rotate(self, angle: float) -> Vector:
        rad = math.radians(angle)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(round(new_x, 2), round(new_y, 2))
