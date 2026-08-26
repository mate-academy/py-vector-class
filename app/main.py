import math


class Vector:
    # write your code here
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> float:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_lenght(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> "Vector":
        lenght = self.get_lenght()
        return Vector(self.x / lenght, self.y / lenght)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitude1 = self.get_lenght()
        magnitude2 = other.get_lenght()
        cos_angle = dot_product / (magnitude1 * magnitude2)
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        return round(math.acos(self.y / self.get_lenght()) * (180 / math.pi))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
