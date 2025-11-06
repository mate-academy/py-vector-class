import math


class Vector:
    def __init__(self, x_vector: float, y_vector: float) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> "Vector | float | None":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return None

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple | list | object,
        end_point: tuple | list | object
    ) -> "Vector":
        if hasattr(start_point, "x") and hasattr(start_point, "y"):
            sx, sy = start_point.x, start_point.y
            sx = float(sx)
            sy = float(sy)
        elif isinstance(start_point, (tuple, list)):
            try:
                sx, sy = start_point
                sx = float(sx)
                sy = float(sy)
            except (TypeError, ValueError):
                raise TypeError(
                    "start_point must be a tuple, list or an object "
                    "with x and y"
                )
        else:
            raise TypeError(
                "start_point must be a tuple, list or an object with x and y"
            )

        if hasattr(end_point, "x") and hasattr(end_point, "y"):
            ex, ey = end_point.x, end_point.y
            ex = float(ex)
            ey = float(ey)
        elif isinstance(end_point, (tuple, list)):
            try:
                ex, ey = end_point
                ex = float(ex)
                ey = float(ey)
            except (TypeError, ValueError):
                raise TypeError(
                    "end_point must be a tuple, list or an object "
                    "with x and y"
                )
        else:
            raise TypeError(
                "end_point must be a tuple, list or an object with x and y"
            )
        dx = ex - sx
        dy = ey - sy
        return cls(dx, dy)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        if self.get_length() == 0:
            return Vector(0, 0)
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot compute angle with zero vector")
        cos_a = dot / (len_self * len_other)
        cos_a = max(-1.0, min(1.0, cos_a))
        angle_deg = math.degrees(math.acos(cos_a))
        return int(round(angle_deg))

    def get_angle(self) -> int:
        angle_rad = math.atan2(-self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        angle_norm = int(round((angle_deg + 360) % 360))
        return angle_norm

    def rotate(self, degrees: float) -> "Vector":
        rad = math.radians(degrees)
        return Vector(
            self.x * math.cos(rad) - self.y * math.sin(rad),
            self.x * math.sin(rad) + self.y * math.cos(rad)
        )
