import math


class Vector:
    def __init__(self, xaxis: float, yaxis: float) -> None:
        self.xaxis = round(xaxis, 2)
        self.yaxis = round(yaxis, 2)

    def __add__(self, other: float) -> None:
        return Vector(self.xaxis + other.xaxis, self.yaxis + other.yaxis)

    def __sub__(self, other: float) -> None:
        return Vector(self.xaxis - other.xaxis, self.yaxis - other.yaxis)

    def __mul__(self, other: float) -> None:
        if isinstance(other, (int, float)):
            return Vector(self.xaxis * other, self.yaxis * other)
        elif isinstance(other, Vector):
            return self.xaxis * other.xaxis + self.yaxis * other.yaxis

    @classmethod
    def create_vector_by_two_points(cls, start_point: float, end_point: float)\
            -> None:
        xaxis = end_point[0] - start_point[0]
        yaxis = end_point[1] - start_point[1]
        return cls(xaxis, yaxis)

    def get_length(self) -> float:
        return math.sqrt(self.xaxis ** 2 + self.yaxis ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.xaxis / length, self.yaxis / length)

    def angle_between(self, other: "Vector") -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.yaxis / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.xaxis * math.cos(radians) - self.yaxis * math.sin(radians)
        new_y = self.xaxis * math.sin(radians) + self.yaxis * math.cos(radians)
        return Vector(new_x, new_y)
