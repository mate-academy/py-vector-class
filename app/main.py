import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: any) -> any:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: any) -> any:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: any) -> any:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Multiplication is only "
                            "supported with a number or another Vector.")

    @classmethod
    def create_vector_by_two_points(cls, start_point: any, end_point: any)\
            -> any:
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> any:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> any:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: any) -> any:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        cos_angle = max(-1, min(1, dot_product / length_product))
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> any:
        magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        cos_theta = self.y / magnitude
        theta_rad = math.acos(cos_theta)
        theta_deg = math.degrees(theta_rad)

        return round(theta_deg)

    def rotate(self, degrees: any) -> any:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta
        return Vector(x_new, y_new)
