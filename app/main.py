import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other_vector: "Vector") -> "Vector":
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector: "Vector") -> "Vector":
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(self, other: object) -> object:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector: "Vector") -> int:
        dot_product = self * other_vector
        length_self = self.get_length()
        length_other = other_vector.get_length()
        if length_self == 0 or length_other == 0:
            return 0
        cosine_angle = dot_product / (length_self * length_other)
        cosine_angle = max(min(cosine_angle, 1), -1)
        angle_deg = math.degrees(math.acos(cosine_angle))
        return round(angle_deg)

    def get_angle(self) -> int:
        angle_deg = (360 - math.degrees(math.atan2(self.x, self.y))) % 360
        return round(angle_deg)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        rotated_x = self.x * cos_theta - self.y * sin_theta
        rotated_y = self.x * sin_theta + self.y * cos_theta
        return Vector(rotated_x, rotated_y)
