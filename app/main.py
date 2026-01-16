import math


class Vector:

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "int | float | Vector") -> "float | Vector":
        if isinstance(other, Vector):
            return float(self.x * other.x + self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        if self.get_length() == 0:
            raise ValueError("zero-length vector")
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> int:
        if not isinstance(other, Vector):
            raise TypeError("other must be Vector")
        len_prod = self.get_length() * other.get_length()
        if len_prod == 0:
            raise ValueError("zero-length vector")
        cos_a = max(-1.0, min(1.0, (self.x * other.x
                                    + self.y * other.y) / (len_prod)))
        return int(round(math.degrees(math.acos(cos_a))))

    def get_angle(self) -> int:
        angle_deg = (90 - math.degrees(math.atan2(self.y, self.x))) % 360
        angle_deg = (-angle_deg) % 360
        return int(round(angle_deg))

    def rotate(self, degrees: int) -> "Vector":
        new_x = (self.x * math.cos(math.radians(degrees))
                 - self.y * math.sin(math.radians(degrees)))
        new_y = (self.x * math.sin(math.radians(degrees))
                 + self.y * math.cos(math.radians(degrees)))
        return Vector(new_x, new_y)
