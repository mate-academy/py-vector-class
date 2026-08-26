import math


class Vector:
    def __init__(self, x_coor: float, y_coor: float) -> None:
        self.x: float = round(x_coor, 2)
        self.y: float = round(y_coor, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> "Vector":
        x_coor: float = end_point[0] - start_point[0]
        y_coor: float = end_point[1] - start_point[1]
        return cls(x_coor, y_coor)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length: float = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product: float = self * other
        length_self: float = self.get_length()
        length_other: float = other.get_length()
        if length_self == 0 or length_other == 0:
            return 0
        cos_angle: float = dot_product / (length_self * length_other)
        angle_rad: float = math.acos(cos_angle)
        angle_deg: int = round(math.degrees(angle_rad))
        return angle_deg

    def get_angle(self) -> int:
        unit_y: "Vector" = Vector(0, 1)
        return self.angle_between(unit_y)

    def rotate(self, degrees: int) -> "Vector":
        radians: float = math.radians(degrees)
        cos_theta: float = math.cos(radians)
        sin_theta: float = math.sin(radians)
        new_x: float = self.x * cos_theta - self.y * sin_theta
        new_y: float = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
