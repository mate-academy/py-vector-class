import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: int | float) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int | float) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: int | float,
                                    end_point: int | float
                                ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: int | float) -> int:
        dot = self * other
        len1 = self.get_length()
        len2 = other.get_length()
        cos_a = dot / (len1 * len2)
        cos_a = max(-1, min(1, cos_a))
        angle = math.degrees(math.acos(cos_a))
        return int(round(angle))

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x, self.y))
        return int(abs(angle))

    def rotate(self, degrees: int | float) -> Vector:
        rad = math.radians(degrees)

        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)
