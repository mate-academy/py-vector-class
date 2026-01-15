import math


class Vector:
    def __init__(self, x_axis: int | float, y_axis: int | float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: float) -> object:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: float) -> object:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> object:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(round((self.x * other), 2),
                          round((self.y * other), 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: float,
                                    end_point: float) -> object:

        x_cr = end_point[0] - start_point[0]
        y_cr = end_point[1] - start_point[1]
        return Vector(x_cr, y_cr)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> float:
        lenght = self.get_length()
        if lenght == 0:
            raise ValueError("Невозможно вычислить нулевой вектор")
        normalize_x = self.x / lenght
        normalize_y = self.y / lenght
        return Vector(normalize_x, normalize_y)

    def angle_between(self, other: float) -> any:
        if not isinstance(other, Vector):
            raise ValueError("Угол вычесляется только между обектами Vector")
        dot_product = self.x * other.x + self.y * other.y
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            raise ValueError("Угол не может быть вычеслен с нулевым вектором")

        cos_theta = dot_product / (length_self * length_other)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_radians = math.acos(cos_theta)
        angle_degrees = round(math.degrees(angle_radians))
        return angle_degrees

    def get_angle(self) -> int:
        angle_radian = math.atan2(self.y, self.x)
        angle_degrees = math.degrees(angle_radian) % 360
        angle_from_y = (90 - angle_degrees) % 360
        return round((360 - angle_from_y) % 360)

    def rotate(self, degrees: float) -> object:
        new_radians = math.radians(degrees)

        new_x = round(
            self.x * math.cos(new_radians) - self.y * math.sin(new_radians), 2
        )

        new_y = round(
            self.x * math.sin(new_radians) + self.y * math.cos(new_radians), 2
        )

        return Vector(new_x, new_y)
