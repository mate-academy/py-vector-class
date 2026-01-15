import math


class Vector:
    def __init__(self, cord_x: float, cord_y: float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be instance of Vector")

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Operand must be instance of Vector")

    def __mul__(self, other: int or float or "Vector") -> float or "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            raise TypeError("Operand must be number or an instance of Vector")

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Length cannot be zero")
        return Vector(self.x / length, self.y / length)

    @staticmethod
    def create_vector_by_two_points(start_point: int or float,
                                    end_point: int or float) -> "Vector":
        if isinstance(start_point, tuple):
            start_point = Vector(*start_point)
        if isinstance(end_point, tuple):
            end_point = Vector(*end_point)
        if (isinstance(start_point, Vector)
                and isinstance(end_point, Vector)):
            return Vector(end_point.x - start_point.x,
                          end_point.y - start_point.y)
        raise TypeError("Start and end points must be instances "
                        "of Vector or tuples")

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            raise ValueError("One of the vectors has zero length")
        cos_a = dot_product / lengths_product
        cos_a = max(-1, min(1, cos_a))
        angle_rad = math.acos(cos_a)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        if angle_deg > 180:
            angle_deg -= 360
        return round(angle_deg) * -1

    def rotate(self, degrees: int) -> "Vector":
        angle_rad = math.radians(degrees)
        cos_angle = math.cos(angle_rad)
        sin_angle = math.sin(angle_rad)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(new_x, new_y)
