import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def get_angle(self) -> float:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)

        return round(abs(angle_deg))

    def angle_between(self, other: Vector) -> int:
        mag1 = self.get_length()
        mag2 = other.get_length()

        if mag1 == 0 or mag2 == 0:
            return 0.0

        dot = self * other
        cos_a = max(-1.0, min(1.0, dot / (mag1 * mag2)))

        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, angle_degrees: float) -> Vector:
        theta = math.radians(angle_degrees)

        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)

        new_x = round(self.x * cos_theta - self.y * sin_theta, 12)
        new_y = round(self.x * sin_theta + self.y * cos_theta, 12)

        return Vector(new_x, new_y)
