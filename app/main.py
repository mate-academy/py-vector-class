import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int | float):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def get_angle(self) -> float:
        angle_degrees = -math.degrees(math.atan2(self.x, self.y))
        angle_degrees = angle_degrees % 360
        return round(angle_degrees)

    def rotate(self, angle_degrees: float) -> Vector:
        radians = math.radians(angle_degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_new, 2), round(y_new, 2))

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other  # use your __mul__ method
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)
