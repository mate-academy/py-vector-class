import math
# flake8: noqa=E741


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | float") -> "Vector | float":
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> "Vector":
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        result = math.degrees(math.acos(cos_a))
        return round(result)

    def get_angle(self) -> int:
        result = self.angle_between(Vector(0, 1))
        return result

    def rotate(self, angle: float | int) -> "Vector":
        rad = angle / 180 * math.pi
        _x = self.x * math.cos(rad) - self.y * math.sin(rad)
        _y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(_x, _y)
