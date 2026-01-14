import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int | float) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> "Vector" and float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(
        start_point: tuple, end_point: tuple
    ) -> "Vector":
        point1 = end_point[0] - start_point[0]
        point2 = end_point[1] - start_point[1]
        return Vector(point1, point2)

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def dot(self, other: "Vector") -> float:
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: "Vector") -> float and int:
        dot_crooss = self.dot(other)
        mag_self = self.get_length()
        mag_other = other.get_length()
        theta = dot_crooss / (mag_self * mag_other)
        theta = max(-1, min(1, theta))
        theta_radians = math.acos(theta)
        theta_degrees = math.degrees(theta_radians)
        return round(theta_degrees)

    def get_angle(self) -> float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
