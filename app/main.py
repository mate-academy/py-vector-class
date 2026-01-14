import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x: float = round(x_coordinate, 2)
        self.y: float = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point:
                                    tuple[float, float]) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        x_diff: float = end_x - start_x
        y_diff: float = end_y - start_y
        return cls(x_diff, y_diff)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length: float = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product: float = self * other
        length_product: float = self.get_length() * other.get_length()
        cos_angle: float = dot_product / length_product
        angle: float = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians: float = math.radians(degrees)
        new_x: float = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y: float = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
