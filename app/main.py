import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other) -> object:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> object:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> object:
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> object:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return cls(cls.x, cls.y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        new_x = self.x / self.get_length()
        new_y = self.y / self.get_length()
        return Vector(new_x, new_y)

    def angle_between(self, other):
        s = (self.x * other.x) + (self.y * other.y)
        m_1 = (self.x ** 2 + self.y ** 2) ** 0.5
        m_2 = (other.x ** 2 + other.y ** 2) ** 0.5
        c = s / (m_1 * m_2)
        return round(math.degrees(math.acos(c)))

    def get_angle(self):
        s = (self.x * 0) + (self.y * self.y)
        m_1 = (0 ** 2 + self.y ** 2) ** 0.5
        m_2 = (0 ** 2 + self.y ** 2) ** 0.5
        c = s / (m_1 * m_2)
        return round(math.degrees(math.acos(c)))

    def rotate(self, degrees: int) -> object:
        x1 = self.x * math.cos(math.radians(degrees)) - self.y * math.sin(math.radians(degrees))
        y1 = self.y * math.cos(math.radians(degrees)) + self.x * math.sin(math.radians(degrees))
        return Vector(x1, y1)
