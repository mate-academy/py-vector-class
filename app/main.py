import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: float) -> float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: float,
                                    end_point: float) -> "Vector":
        x1, y1 = start_point
        x2, y2 = end_point
        dx = x2 - x1
        dy = y2 - y1
        return cls(dx, dy)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        nx = self.x / length
        ny = self.y / length
        return Vector(nx, ny)

    def angle_between(self, vector : "Vector") -> float:
        dot = self.x * vector.x + self.y * vector.y
        length_1 = self.get_length()
        length_2 = vector.get_length()
        if length_1 == 0 or length_2 == 0:
            return 0
        cos_a = dot / (length_1 * length_2)
        cos_a = max(-1.0, min(1.0, cos_a))
        a_rad = math.acos(cos_a)
        a_deg = math.degrees(a_rad)
        return round(a_deg)

    def get_angle(self) -> int:
        if self.x == 0 and self.y == 0:
            return 0
        theta = math.degrees(math.atan2(self.x, self.y))
        angle = (-theta) % 360
        return int(round(angle))

    def rotate(self, angle: float) -> "Vector":
        rad = math.radians(angle)
        cos_t = math.cos(rad)
        sin_t = math.sin(rad)
        new_x = self.x * cos_t - self.y * sin_t
        new_y = self.x * sin_t + self.y * cos_t
        return Vector(new_x, new_y)
