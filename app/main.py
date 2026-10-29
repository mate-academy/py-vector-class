import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: "float | Vector") -> "Vector | float":
        if not isinstance(other, Vector):
            return Vector((self.x * other), (self.y * other))
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: "Vector") -> int:
        if isinstance(other, Vector):
            len_self = self.get_length()
            len_other = other.get_length()
            cos_a = (self * other) / (len_self * len_other)
            cos_a = max(-1, min(1, cos_a))
            angle_deg = math.degrees(math.acos(cos_a))
            return round(angle_deg)
        return NotImplemented

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        cos_a = max(-1, min(1, cos_a))
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def rotate(self, degree: float) -> "Vector":
        radian = math.radians(degree)
        return Vector(self.x * math.cos(radian) - self.y * math.sin(radian),
                      self.x * math.sin(radian) + self.y * math.cos(radian))
