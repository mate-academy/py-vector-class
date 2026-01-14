import math


class Vector:
    def __init__(self, x_coord: [float, int], y_coord: [float, int]) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x,
                          self.y - other.y)

    def __mul__(self, other: [float, int, "Vector"]) -> [float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        if isinstance(other, Vector):
            res = (self.x * other.x) + (self .y * other.y)
            return res

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return ((self.x)**2 + (self.y)**2)**0.5

    def get_normalized(self) -> "Vector":
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: "Vector") -> int:
        res_1 = self * vector
        res_2 = self.get_length() * vector.get_length()
        if res_2 == 0:
            return 0
        cos_a = res_1 / res_2
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        vec = Vector(0, 1)
        return self.angle_between(vec)

    def rotate(self, degree: int) -> "Vector":
        radian = math.radians(degree)
        res_x = self.x * math.cos(radian) - self.y * math.sin(radian)
        res_y = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(res_x, res_y)
