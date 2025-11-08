import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa
        self.x: float = round(x, 2)
        self.y: float = round(y, 2)  # noqa

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: float) -> "Vector" or float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: float,
                                    end_point: float
                                    ) -> "Vector":
        return cls(round(end_point[0] - start_point[0], 2),
                   round(end_point[1] - start_point[1], 2))

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        dot = self.x * other.x + self.y * other.y
        mag_self = (self.x ** 2 + self.y ** 2) ** 0.5
        mag_other = (other.x ** 2 + other.y ** 2) ** 0.5
        cos_a = dot / (mag_self * mag_other)
        return round(math.degrees(math.acos(cos_a)), 0)

    def get_angle(self) -> float:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        return round(abs(angle_deg))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(round(new_x, 2), round(new_y, 2))
