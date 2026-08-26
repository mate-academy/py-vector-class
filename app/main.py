import math


class Vector:
    def __init__(self, cord_x: float, cord_y: float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return Vector(self.x + other, self.y + other)

    def __sub__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return Vector(self.x - other, self.y - other)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        mag1 = math.sqrt(self.x ** 2 + self.y ** 2)
        mag2 = math.sqrt(other.x ** 2 + other.y ** 2)
        if mag1 == 0 or mag2 == 0:
            return 0
        else:
            cos_a = max(-1.0, min(1.0, dot_product / (mag1 * mag2)))
            return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return int(round(abs(math.degrees(math.atan2(self.x, self.y)))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos, sin = math.cos(radians), math.sin(radians)
        cord_x = self.x * cos - self.y * sin
        cord_y = self.x * sin + self.y * cos
        return Vector(round(cord_x, 2), round(cord_y, 2))
